# CLAUDE.md

This file provides working guidance for the thesis project in this directory.

## Project Scope

- Project: HUST master thesis (searchable encryption)
- Main file: `main.tex`
- Active chapters:
  - `body/chapter/intro.tex`
  - `body/chapter/bf.tex`
  - `body/chapter/commitment.tex`
  - `body/chapter/experiments.tex`
  - `body/chapter/conclusion.tex`

## Current Writing Baseline (2026-02-25 精修后)

1. `intro.tex`: mostly drafted, needs polishing and citation checks.
2. `bf.tex`: 安全证明已精修（命题 2 归约补全、新鲜性形式化、VQ-Sound 条件性质），后半部分 QTree 构造细节待补。
3. `commitment.tex`: 初稿+精修完成——TSet 认证加密升级、AB-Sound 扩展、CV 实验完整化、6 处归约模拟能力补全、VSSE 对比表修复。
4. `experiments.tex`: evaluation structure exists, data/results pending.
5. `conclusion.tex`: outline only.

## Build

Recommended compile chain:

```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
bibtex main
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
```

## Writing Rules for This Thesis

### 结构与形式化

1. Keep notation consistent across chapters (system entities, leakage, correctness, verifiability).
2. For each new claim, provide either a formal argument or a citation.
3. In Chapter 2 and 3, always separate:
   - threat model
   - construction
   - correctness/verifiability analysis
   - leakage discussion
4. For Chapter 4, ensure each figure/table has:
   - metric definition
   - baseline comparison
   - concise interpretation
5. Security proof sections must follow "game/hybrid + reduction": specify adversary model, advantage function, reduction algorithm, bad events, and final bound derivation.
6. Each reduction algorithm $\mathcal{B}_i$ must explicitly state: (a) which keys it holds, (b) which key is missing (replaced by oracle access), (c) how it simulates the full experiment interaction. A bare cross-reference ("same as Proposition X") is insufficient.
7. When a security property is conditional (depends on another property's guarantee), the experiment definition must include an explicit precondition, and the proposition statement must be labeled as conditional.
8. When payload integrity is required, use authenticated encryption (AE/INT-CTXT), not plain symmetric encryption (SE/CPA).
9. If data, theorem constants, or empirical numbers are missing, mark placeholders as `【待补充】` and do not fabricate.

### 禁止语类

7. Do not use meta-writing phrases in chapter text (e.g., "for writing style", "for ease of exposition", "为便于叙述", "下文将介绍").
8. Replace any writing-process narration with technical statements about model, assumptions, or claims.
9. Avoid template AI phrasing, including "本文将/我们将/总之/显而易见/值得注意的是/随着……发展".
10. Do not use vague adjectives (e.g., "huge", "revolutionary", "very important") without formal support.
11. Keep paragraph tone review-ready: technical and constrained, no conversational wording.

### 领域用语规范（密码学论文特有）

12. 禁止软件工程用语进入密码学描述：不得使用"工程可用性"、"工程可落地性"、"接口"、"解耦"、"数据平面"、"在实现层面"等软件/系统工程术语描述密码学构造或安全性质。
13. 禁止政策/营销语言：不得使用"数字经济核心基础设施"、"合规治理"、"信任度与采纳意愿"、"数据要素流通"等政策宣传或市场营销表述。
14. 禁止教科书式分类枚举：不得以"从…到…再到…"的递进句式做面面俱到的文献综述导语；文献综述应直接按技术维度组织。
15. "可忽略"（negligible）专指关于安全参数 $\lambda$ 的可忽略函数 $\mathsf{negl}(\lambda)$，不得用于描述假阳性率、性能开销等非安全参数量。
16. 密码学原语（PRF, Hash, OPRF, AE 等）在"符号约定"节给出类型签名与安全性要求，不在该节讨论原语与具体方案的绑定关系；方案绑定在后续构造节中阐述。
17. 协议交互流程节应采用通用 SSE 语言描述，Nomos 等具体方案的令牌结构（stag/bstag/xtrap/bxtrap/env）仅在该方案的专属小节中展开。

### 行文风格

18. 避免短句堆砌：每个算法或协议步骤的描述应至少包含完整的输入-操作-输出语义，不得仅用一句话概括。
19. 算法签名应标注输出类型（如 $\mathsf{Setup}(1^\lambda)\to(\mathsf{K},\mathsf{st},\mathsf{EDB})$），使形式定义自洽。
20. 图表后的正文段落不应复述图表已展示的信息，而应阐述图表对后续内容的承载关系或设计启示。
21. 符号表采用统一平铺格式，无需按"实体/原语/索引"等类别分组标注。

## Citation Hygiene

- Bibliography file: `ref/thesis.bib`
- Check every cited key exists in `thesis.bib` before final compile.
- Prefer consistent venue naming and author formatting.

## Collaboration Notes

- When editing chapter text, update progress in root workspace docs:
  - `../控制面板.md`
  - `../01-论文生产/选题管理/00-选题记录.md`
  - `../记忆库/论文系统初始化总结.md`
- For PDF reading and quoting prep, prefer Markdown papers in:
  - `../01-论文生产/素材库/论文Markdown库/`
  - default format is Xray-style extraction (`ljg-xray-paper`), not raw full-text dump

## 同步原则（最高优先级）

- 本项目的最终目标是完成 LaTeX 论文编写。所有在方法论 Markdown 文件（`../01-论文生产/方法论/` 下）中做出的修改，必须同步到 LaTeX 侧对应的 `.tex` 文件中。
- 如果 LaTeX 侧尚无对应内容，则创建新的 LaTeX 内容（新节、新表、新定义等）。
- 修复问题列表（`../01-论文生产/方法论/问题列表.md`）中的每个问题时，完成 Markdown 侧修改后必须立即检查并同步 LaTeX 侧，确保两侧一致。
- 每次修改完成后应编译验证 LaTeX 无新增错误。
