#!/usr/bin/env python3
"""
Utility script to extract 20-paper batches from papers.csv, fetch abstracts,
and persist them as JSON for collaborative screening.

Usage:
    python scripts/process_batch.py --batch 1

This will create out/batches/batch_001.json with the following schema:
[
  {
    "row_index": 1,
    "title": "...",
    "url": "...",
    "year": "2022",
    "citations": "123",
    "authors": "...",
    "csv_abstract": "...",
    "fetched_abstract": "...",  # may be None if fetch fails
    "fetch_status": "ok" | "error:<message>"
  },
  ...
]

The helper is intentionally lightweight so different reviewers can process
disjoint batches in parallel without re-implementing the plumbing.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import textwrap
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from html import unescape
from pathlib import Path
from typing import List, Optional

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "papers.csv"
OUTPUT_DIR = ROOT / "out" / "batches"

ARXIV_RE = re.compile(
    r'<span class="descriptor">Abstract:</span>(.*?)</blockquote>', re.S
)
NEURIPS_RE = re.compile(r"Abstract\s*</h4>\s*<p>(.*?)</p>", re.S)


@dataclass
class PaperRecord:
    row_index: int
    title: str
    url: str
    year: str
    citations: str
    authors: str
    csv_abstract: str
    fetched_abstract: Optional[str]
    fetch_status: str


def _clean_html(html: str) -> str:
    html = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
    html = re.sub(r"<style.*?</style>", " ", html, flags=re.S)
    html = re.sub(r"<.*?>", " ", html)
    return unescape(" ".join(html.split()))


def fetch_abstract(url: str) -> tuple[Optional[str], str]:
    adjusted_url = url
    if "biorxiv.org/content/" in url and url.endswith(".pdf"):
        adjusted_url = url.split(".pdf")[0]

    if not adjusted_url:
        return None, "error:missing-url"
    req = urllib.request.Request(
        adjusted_url, headers={"User-Agent": "Mozilla/5.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            content_type = resp.info().get_content_type()
            data = resp.read(200_000)
    except urllib.error.HTTPError as exc:
        return None, f"error:http:{exc.code}"
    except Exception as exc:
        return None, f"error:{exc.__class__.__name__}"

    if content_type == "application/pdf":
        return None, "error:pdf-content"

    html = data.decode("utf-8", "ignore")
    if "arxiv.org/abs/" in adjusted_url:
        match = ARXIV_RE.search(html)
        if match:
            cleaned = _clean_html(match.group(1))
            return cleaned, "ok"
    if "proceedings.neurips.cc" in adjusted_url:
        match = NEURIPS_RE.search(html)
        if match:
            cleaned = _clean_html(match.group(1))
            return cleaned, "ok"
    return _clean_html(html), "ok"


def read_batch(batch_index: int) -> List[PaperRecord]:
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"papers.csv not found at {CSV_PATH}")

    start = (batch_index - 1) * 20
    end = start + 20

    records: List[PaperRecord] = []
    with CSV_PATH.open(newline="") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            if idx < start:
                continue
            if idx >= end:
                break

            csv_abstract = row.get("Abstract", "").strip()
            title = row.get("Title", "").strip()
            url = row.get("ArticleURL", "").strip()
            year = row.get("Year", "").strip()
            citations = row.get("Cites", "").strip()
            authors = row.get("Authors", "").strip()

            fetched_abstract, status = fetch_abstract(url)

            records.append(
                PaperRecord(
                    row_index=idx + 1,
                    title=title,
                    url=url,
                    year=year,
                    citations=citations,
                    authors=authors,
                    csv_abstract=csv_abstract,
                    fetched_abstract=fetched_abstract,
                    fetch_status=status,
                )
            )
    return records


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prepare a batch of 20 papers from papers.csv."
    )
    parser.add_argument(
        "--batch",
        type=int,
        required=True,
        help="1-based batch index (batch 1 = rows 1-20, batch 2 = rows 21-40, ...)",
    )
    parser.add_argument(
        "--emit",
        choices=["json", "stdout"],
        default="json",
        help="Whether to write to out/batches or print to stdout",
    )
    args = parser.parse_args()

    if args.batch < 1:
        parser.error("batch must be >= 1")

    records = read_batch(args.batch)
    if not records:
        print("No records found for the requested batch.", file=sys.stderr)
        sys.exit(1)

    if args.emit == "stdout":
        for rec in records:
            print(f"{rec.row_index:04d}: {rec.title} [{rec.fetch_status}]")
            abstract = rec.fetched_abstract or rec.csv_abstract or "<no abstract>"
            print(textwrap.fill(abstract, 100))
            print("-" * 60)
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"batch_{args.batch:03d}.json"
    with output_path.open("w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in records], f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(records)} records to {output_path}")


if __name__ == "__main__":
    main()
