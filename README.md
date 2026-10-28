# Artificial Intelligence Laboratory (AI Lab)
**Course:** AI Laboratory $\cdot$ CSE-AIML  
**Student Name:** Soumya Ranjan  
**University Roll / Reg. No:** `25CSEAIML046`  
**Repository:** [https://github.com/Soumya-19-Ranjan/AI_LAB_25CSEAIML046.git](https://github.com/Soumya-19-Ranjan/AI_LAB_25CSEAIML046.git)

---

## 📌 Submission Overview

This repository contains the complete source code, test inputs, execution outputs, and comprehensive LaTeX (`.tex`) documentation for all **13 AI Lab Experiments** in compliance with the academic submission guidelines.

---

## 📂 Repository Structure

```text
AI_LAB_25CSEAIML046/
├── AI_Lab_Report_25CSEAIML046.tex  # Complete Master Lab Record (Cover page, Index, Code, Outputs)
├── README.md                       # Comprehensive documentation & execution guide
├── generate_outputs_and_tex.py     # Automation script to execute all experiments and build TeX files
│
├── outputs/                        # Individual and consolidated output records
│   ├── all_experiments_output.tex  # Consolidated outputs in LaTeX format
│   ├── exp01_bfs_output.tex        # Exp 1 LaTeX output snippet
│   ├── exp01_bfs_output.txt        # Exp 1 Raw terminal output
│   ├── exp02_dfs_output.tex        # Exp 2 LaTeX output snippet
│   ├── exp02_dfs_output.txt        # Exp 2 Raw terminal output
│   ├── exp03_ucs_output.tex        # Exp 3 LaTeX output snippet
│   ├── exp03_ucs_output.txt        # Exp 3 Raw terminal output
│   ├── exp04_dls_output.tex        # Exp 4 LaTeX output snippet
│   ├── exp04_dls_output.txt        # Exp 4 Raw terminal output
│   ├── exp05_astar_output.tex      # Exp 5 LaTeX output snippet
│   ├── exp05_astar_output.txt      # Exp 5 Raw terminal output
│   ├── exp06_hill_climbing_output.tex # Exp 6 LaTeX output snippet
│   ├── exp06_hill_climbing_output.txt # Exp 6 Raw terminal output
│   ├── exp07_tsp_output.tex        # Exp 7 LaTeX output snippet
│   ├── exp07_tsp_output.txt        # Exp 7 Raw terminal output
│   ├── exp08_eight_queen_output.tex# Exp 8 LaTeX output snippet
│   ├── exp08_eight_queen_output.txt# Exp 8 Raw terminal output
│   ├── exp09_water_jug_output.tex  # Exp 9 LaTeX output snippet
│   ├── exp09_water_jug_output.txt  # Exp 9 Raw terminal output
│   ├── exp10_tic_tac_toe_output.tex# Exp 10 LaTeX output snippet
│   ├── exp10_tic_tac_toe_output.txt# Exp 10 Raw terminal output
│   ├── exp11_minimax_output.tex    # Exp 11 LaTeX output snippet
│   ├── exp11_minimax_output.txt    # Exp 11 Raw terminal output
│   ├── exp12_alpha_beta_output.tex # Exp 12 LaTeX output snippet
│   ├── exp12_alpha_beta_output.txt # Exp 12 Raw terminal output
│   ├── exp13_block_world_output.tex# Exp 13 LaTeX output snippet
│   └── exp13_block_world_output.txt# Exp 13 Raw terminal output
│
└── [Source Code Files]
    ├── BFS.py                      # Exp 1: Breadth First Search
    ├── DFS.py                      # Exp 2: Depth First Search
    ├── ucs.py                      # Exp 3: Uniform Cost Search
    ├── dls.py                      # Exp 4: Depth Limited Search
    ├── A_star.py                   # Exp 5: A* Search Algorithm
    ├── HILL_CLIMBING.py            # Exp 6: Hill Climbing Search
    ├── TSP.py                      # Exp 7: Travelling Salesman Problem
    ├── Eight_Queen.py              # Exp 8: 8-Queens Problem (Backtracking)
    ├── Water_jug.py                # Exp 9: Water Jug Problem (State Space)
    ├── Tic_Tac_Toe.py              # Exp 10: Tic-Tac-Toe Game
    ├── minmax.py                   # Exp 11: Minimax Adversarial Search
    ├── Alpha_Beta_pruning.py       # Exp 12: Alpha-Beta Pruning
    └── block_world.py              # Exp 13: Blocks World Planning Problem
```

---

## 🧪 Experiments Index & Descriptions

| Exp. # | Experiment Title | Source File | Technique / Algorithm | Output File |
|:---:|:---|:---|:---|:---|
| **01** | Breadth First Search (BFS) | [`BFS.py`](BFS.py) | Uninformed Queue Search (FIFO) | [`exp01_bfs_output.tex`](outputs/exp01_bfs_output.tex) |
| **02** | Depth First Search (DFS) | [`DFS.py`](DFS.py) | Uninformed Stack Search (LIFO) | [`exp02_dfs_output.tex`](outputs/exp02_dfs_output.tex) |
| **03** | Uniform Cost Search (UCS) | [`ucs.py`](ucs.py) | Dijkstra-style Priority Queue Search | [`exp03_ucs_output.tex`](outputs/exp03_ucs_output.tex) |
| **04** | Depth Limited Search (DLS) | [`dls.py`](dls.py) | Constrained Depth Backtracking | [`exp04_dls_output.tex`](outputs/exp04_dls_output.tex) |
| **05** | A* Search Algorithm | [`A_star.py`](A_star.py) | Heuristic Pathfinding ($f = g + h$) | [`exp05_astar_output.tex`](outputs/exp05_astar_output.tex) |
| **06** | Hill Climbing Algorithm | [`HILL_CLIMBING.py`](HILL_CLIMBING.py) | Local Optimization / Greedy Search | [`exp06_hill_climbing_output.tex`](outputs/exp06_hill_climbing_output.tex) |
| **07** | Travelling Salesman Problem | [`TSP.py`](TSP.py) | Permutation / Exhaustive Tour Search | [`exp07_tsp_output.tex`](outputs/exp07_tsp_output.tex) |
| **08** | 8-Queens Problem | [`Eight_Queen.py`](Eight_Queen.py) | Backtracking Constraint Satisfaction | [`exp08_eight_queen_output.tex`](outputs/exp08_eight_queen_output.tex) |
| **09** | Water Jug Problem | [`Water_jug.py`](Water_jug.py) | State Space Search with BFS | [`exp09_water_jug_output.tex`](outputs/exp09_water_jug_output.tex) |
| **10** | Tic-Tac-Toe Game | [`Tic_Tac_Toe.py`](Tic_Tac_Toe.py) | Turn-based Game State Validation | [`exp10_tic_tac_toe_output.tex`](outputs/exp10_tic_tac_toe_output.tex) |
| **11** | Minimax Algorithm | [`minmax.py`](minmax.py) | Adversarial Game Tree Evaluation | [`exp11_minimax_output.tex`](outputs/exp11_minimax_output.tex) |
| **12** | Alpha-Beta Pruning | [`Alpha_Beta_pruning.py`](Alpha_Beta_pruning.py) | Branch Cutoff Minimax Optimization | [`exp12_alpha_beta_output.tex`](outputs/exp12_alpha_beta_output.tex) |
| **13** | Blocks World Problem | [`block_world.py`](block_world.py) | Classical AI Planning using BFS | [`exp13_block_world_output.tex`](outputs/exp13_block_world_output.tex) |

---

## 🚀 Execution Guide

You can run any experiment individually using Python:

```bash
# 1. Breadth First Search (BFS)
python BFS.py

# 2. Depth First Search (DFS)
python DFS.py

# 3. Uniform Cost Search (UCS)
python ucs.py

# 4. Depth Limited Search (DLS)
python dls.py

# 5. A* Search Algorithm
python A_star.py

# 6. Hill Climbing Algorithm
python HILL_CLIMBING.py

# 7. Travelling Salesman Problem (TSP)
python TSP.py

# 8. 8-Queens Problem
python Eight_Queen.py

# 9. Water Jug Problem
python Water_jug.py

# 10. Tic-Tac-Toe Game
python Tic_Tac_Toe.py

# 11. Minimax Algorithm
python minmax.py

# 12. Alpha-Beta Pruning
python Alpha_Beta_pruning.py

# 13. Blocks World Problem
python block_world.py
```

To automatically re-execute all 13 experiments and regenerate all individual and master LaTeX output documents:
```bash
python generate_outputs_and_tex.py
```

---

## 📄 LaTeX Documentation

1. **Master Lab Report:** [`AI_Lab_Report_25CSEAIML046.tex`](AI_Lab_Report_25CSEAIML046.tex)
   - Publication-quality LaTeX document.
   - Includes custom Cover Page, Table of Contents, Theory/Algorithm, full syntax-highlighted Python Code, Input Specifications, Verbatim Terminal Outputs, and Conclusions for all 13 experiments.
   - Can be directly compiled via `pdflatex` or uploaded to [Overleaf](https://www.overleaf.com/).

2. **Compiled Outputs Document:** [`outputs/all_experiments_output.tex`](outputs/all_experiments_output.tex)
   - Dedicated compilation focused specifically on the terminal execution outputs of all experiments.

3. **Individual Output Snippets:** Located in [`outputs/`](outputs/) for modular inclusion in institutional reports.

---

## ✅ Submission Checklist Verification

- [x] All 13 AI Lab source code files tested and operational.
- [x] Execution outputs generated and organized in LaTeX (`.tex`) format.
- [x] Master laboratory manual (`AI_Lab_Report_25CSEAIML046.tex`) created.
- [x] Individual `.tex` and `.txt` output files stored in `outputs/`.
- [x] Repository link verified: `https://github.com/Soumya-19-Ranjan/AI_LAB_25CSEAIML046.git`.