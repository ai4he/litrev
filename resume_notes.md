### SLR status (Math+LLM)
- Papers processed: rows 1-120 (batches 1-6). Relevant works integrated into `main.tex` and `changes.bib`.
- Next batch: rows 121-140 (batch 7).

### Pending screening (rows 121-140)
121. A mechanistic interpretation of arithmetic reasoning in language models using causal mediation analysis — https://arxiv.org/abs/2305.15054
122. Jiuzhang 2.0: A unified Chinese pre-trained language model for multi-task mathematical problem solving — https://dl.acm.org/doi/abs/10.1145/3580305.3599850
123. Democratizing reasoning ability: Tailored learning from large language model — https://arxiv.org/abs/2310.13332
124. Llemma: An open language model for mathematics — https://arxiv.org/abs/2310.10631
125. UniMath: A foundational and multimodal mathematical reasoner — https://aclanthology.org/2023.emnlp-main.440/
126. ChatCoT: Tool-augmented chain-of-thought reasoning on chat-based large language models — https://arxiv.org/abs/2305.14323
127. MAmmoTH: Building math generalist models through hybrid instruction tuning — https://arxiv.org/abs/2309.05653
128. Plan-and-Solve Prompting: Improving zero-shot chain-of-thought reasoning by large language models — https://arxiv.org/abs/2305.04091
129. Evaluation of basic mathematical abilities of neural networks — https://thesis.unipd.it/handle/20.500.12608/52790
130. AI for mathematics: A cognitive science perspective — https://arxiv.org/abs/2310.13021
131. Evaluation of Large Scale Language Models on Solving Math Word Problems with Difficulty Grading — https://ieeexplore.ieee.org/abstract/document/10391224/
132. MAF: Multi-aspect feedback for improving reasoning in large language models — https://arxiv.org/abs/2310.12426
133. Query and response augmentation cannot help out-of-domain math reasoning generalization — https://openreview.net/forum?id=N1hk66bz5m
134. MuggleMath: Assessing the impact of query and response augmentation on math reasoning — https://arxiv.org/abs/2310.05506
135. PAL: Program-Aided Language Models — https://proceedings.mlr.press/v202/gao23f
136. How does GPT-2 compute greater-than?: Interpreting mathematical abilities in a pre-trained language model — https://proceedings.neurips.cc/paper_files/paper/2023/hash/efbba7719cc5172d175240f24be11280-Abstract-Conference.html
137. Adapting large language models for education: Foundational capabilities, potentials, and challenges — https://www.academia.edu/download/119620398/2401.08664.pdf
138. Automatic model selection with large language models for reasoning — https://arxiv.org/abs/2305.14333
139. Glore: Evaluating logical reasoning of large language models — https://arxiv.org/abs/2310.09107
140. Can large language models explain themselves? A study of LLM-generated self-explanations — https://arxiv.org/abs/2310.11207

### Actions when resuming
1. Run `python3 scripts/process_batch.py --batch 7 --emit json` to fetch abstracts for rows 121-140.
2. Evaluate relevance (math+LLM algorithmic/dataset contributions). For relevant papers, check `references.bib`; add missing BibTeX entries to `changes.bib`, integrate citations into `main.tex`, and set the `SELECTED` flag in `papers.csv` (`1` for included, `0` otherwise).
3. Continue sequential batches until all 2068 papers are reviewed (current progress: 120 processed).
4. Maintain Overleaf-only compilation workflow (no local latexmk required).
