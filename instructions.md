# Working Instructions (Math + LLM Literature Review)

These notes capture the user’s requirements so the task can be resumed at any time without re-reading prior conversations.

1. **Repository & Environment**
   - Work in the GitHub repo `https://github.com/ai4he/litrev.git` (local path `/Users/carlos/Documents/projects/math`).
   - Use Overleaf for building the LaTeX document; no local `latexmk` runs are necessary unless explicitly requested.

2. **Files of Interest**
   - `main.tex`: ACM-style survey that must be updated with new citations and discussion.
   - `references.bib`: canonical bibliography file.
   - `changes.bib`: staging area for new BibTeX entries identified during screening.
   - `papers.csv`: master list of papers for the systematic literature review (SLR).
   - `scripts/process_batch.py`: helper for fetching 20-paper batches and abstracts.
   - `resume_notes.md`: snapshot of current progress, next batch index, and resume steps.

3. **Systematic Review Procedure**
   - Process `papers.csv` in batches of 20 entries.
   - For each batch:
     1. Fetch abstracts (`python3 scripts/process_batch.py --batch N --emit json` or `stdout`).
     2. Determine relevance: keep papers contributing algorithms, datasets, or evaluations at the intersection of mathematics and large language models. Skip general surveys or off-topic works unless they add direct value to the survey scope.
     3. Check whether each relevant paper already exists in `references.bib`. If missing, append a clean BibTeX entry to `changes.bib` (ASCII only, sorted keys optional).
     4. Update `main.tex` with concise discussion of the new work, citing the new BibTeX key via `\cite{...}`.
     5. Record decisions in `papers.csv` by updating the `SELECTED` column (`1` for included papers, `0` for screened-out papers, blank for batches not yet reviewed).
   - Continue sequential batches until all `papers.csv` entries (currently 2068) are reviewed.

4. **Git Workflow**
   - Commit regularly with descriptive messages (e.g., `docs: integrate batch N insights`).
   - Push to `origin/main` when a batch or logical unit is complete.

5. **Current Progress (as of latest commit)**
   - Batches 1–5 (rows 1–100) processed and integrated.
   - Next batch to screen: Batch 6 (rows 101–120); see `resume_notes.md` for queued titles and URLs.

