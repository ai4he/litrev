### SLR status (Math+LLM)
- Papers processed: rows 1-100 (batches 1-5). Relevant works integrated into `main.tex` and `changes.bib`.
- Next batch: rows 101-120 (batch 6).

### Pending screening (rows 101-120)
101. Numerical reasoning in NLP: Challenges, innovations, and strategies for handling mathematical equivalency — https://repository.kulib.kyoto-u.ac.jp/dspace/bitstream/2433/285863/1/djohk00840.pdf
102. Tora: A tool-integrated reasoning agent for mathematical problem solving — https://arxiv.org/abs/2309.17452
103. Mathcoder: Seamless code integration in LLMs for enhanced mathematical reasoning — https://arxiv.org/abs/2310.03731
104. Olapa-MCoT: Enhancing the Chinese Mathematical Reasoning Capability of LLMs — https://arxiv.org/abs/2312.17535
105. Reasoning arithmetic word problems entailing implicit relations based on the chain-of-thought model — https://researchers.mq.edu.au/en/publications/reasoning-arithmetic-word-problems-entailing-implicit-relations-b
106. Rewriting Math Word Problems with Large Language Models — https://eric.ed.gov/?id=ED655931
107. GPT can solve mathematical problems without a calculator — https://arxiv.org/abs/2309.03241
108. From good to great: Improving math reasoning with tool-augmented interleaf prompting — https://arxiv.org/abs/2401.05384
109. FinanceMath: Knowledge-intensive math reasoning in finance domains — https://arxiv.org/abs/2311.09797
110. GeomVerse: A systematic evaluation of large models for geometric reasoning — https://arxiv.org/abs/2312.12241
111. A symbolic framework for evaluating mathematical reasoning and generalisation with transformers — https://arxiv.org/abs/2305.12563
112. Tuning ChatGPT mathematical reasoning limitations and failures with process supervision — https://www.noveltyjournals.com/upload/paper/TUNING%20CHATGPT%20MATHEMATICAL-29082023-1.pdf
113. Turning large language models into cognitive models — https://arxiv.org/abs/2306.03917
114. Chain-of-thought reasoning in tabular language models — https://aclanthology.org/2023.findings-emnlp.734/
115. Fill in the blank: Exploring and enhancing LLM capabilities for backward reasoning in math word problems — https://arxiv.org/abs/2310.01991
116. Large language models cannot self-correct reasoning yet — https://arxiv.org/abs/2310.01798
117. Mathematical capabilities of ChatGPT — https://proceedings.neurips.cc/paper_files/paper/2023/hash/58168e8a92994655d6da3939e7cc0918-Abstract-Datasets_and_Benchmarks.html
118. Making large language models better reasoners with alignment — https://arxiv.org/abs/2309.02144
119. Logic-LM: Empowering large language models with symbolic solvers for faithful logical reasoning — https://arxiv.org/abs/2305.12295
120. Large language models are versatile decomposers: Decomposing evidence and questions for table-based reasoning — https://dl.acm.org/doi/abs/10.1145/3539618.3591708

### Actions when resuming
1. Run `python3 scripts/process_batch.py --batch 6 --emit json` to fetch abstracts for rows 101-120.
2. Evaluate relevance (math+LLM algorithmic/dataset contributions). For relevant papers, check `references.bib`; add missing BibTeX entries to `changes.bib` and integrate citations into `main.tex`.
3. Continue sequential batches until all 2068 papers are reviewed (current progress: 100 processed).
4. Maintain Overleaf-only compilation workflow (no local latexmk required).
