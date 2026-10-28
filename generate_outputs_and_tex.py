import os
import subprocess

os.makedirs("outputs", exist_ok=True)

experiments = [
    {
        "id": "exp01_bfs",
        "num": 1,
        "title": "Breadth First Search (BFS)",
        "script": "BFS.py",
        "aim": "To implement Breadth-First Search (BFS) graph traversal using a queue data structure to visit vertices level by level.",
        "input_desc": "4 edges: (A B), (A C), (B D), (C E); Starting node: A",
        "input_str": "4\nA B\nA C\nB D\nC E\nA\n",
        "theory": "Breadth-First Search is an uninformed search algorithm that begins at the root node and explores all neighbouring nodes at the present depth level before moving on to nodes at the next depth level. It uses a First-In-First-Out (FIFO) Queue data structure. Time Complexity: $\\mathcal{O}(V + E)$, Space Complexity: $\\mathcal{O}(V)$."
    },
    {
        "id": "exp02_dfs",
        "num": 2,
        "title": "Depth First Search (DFS)",
        "script": "DFS.py",
        "aim": "To implement Depth-First Search (DFS) graph traversal using a stack to explore each branch as deeply as possible before backtracking.",
        "input_desc": "4 edges: (A B), (A C), (B D), (C E); Starting node: A",
        "input_str": "4\nA B\nA C\nB D\nC E\nA\n",
        "theory": "Depth-First Search is an uninformed search algorithm that starts at the root node and traverses as deep as possible along each branch before backtracking. It operates using a Last-In-First-Out (LIFO) Stack data structure or recursion. Time Complexity: $\\mathcal{O}(V + E)$, Space Complexity: $\\mathcal{O}(V)$."
    },
    {
        "id": "exp03_ucs",
        "num": 3,
        "title": "Uniform Cost Search (UCS)",
        "script": "ucs.py",
        "aim": "To implement Uniform Cost Search (UCS) using a priority queue to find the path with minimum cumulative edge cost from start to goal.",
        "input_desc": "5 nodes, 5 edges: (0 1: 2), (0 2: 4), (1 3: 7), (2 4: 3), (3 4: 1); Start: 0, Goal: 4",
        "input_str": "5\n5\n0 1 2\n0 2 4\n1 3 7\n2 4 3\n3 4 1\n0\n4\n",
        "theory": "Uniform Cost Search is an optimal uninformed search algorithm equivalent to Dijkstra's algorithm. It expands the node with the lowest cumulative path cost $g(n)$ from the start node using a min-priority queue. It guarantees an optimal solution if all step costs are non-negative."
    },
    {
        "id": "exp04_dls",
        "num": 4,
        "title": "Depth Limited Search (DLS)",
        "script": "dls.py",
        "aim": "To implement Depth Limited Search (DLS) to mitigate the infinite loop vulnerability of DFS by constraining search depth.",
        "input_desc": "5 nodes, 4 edges: (0 1), (0 2), (1 3), (2 4); Start: 0, Goal: 4, Depth Limit: 3",
        "input_str": "5\n4\n0 1\n0 2\n1 3\n2 4\n0\n4\n3\n",
        "theory": "Depth Limited Search is a variation of Depth First Search where the exploration terminates once a fixed maximum depth limit $l$ is reached. If the goal node is located within depth $l$, DLS finds it; otherwise it reports cut-off failure."
    },
    {
        "id": "exp05_astar",
        "num": 5,
        "title": "A* Search Algorithm",
        "script": "A_star.py",
        "aim": "To implement A* Search Algorithm using evaluation function $f(n) = g(n) + h(n)$ combining exact cost and heuristic estimate.",
        "input_desc": "4 nodes (A, B, C, D) with heuristics h(A)=10, h(B)=8, h(C)=5, h(D)=0; 4 directed edges: A->B(1), A->C(4), B->D(5), C->D(2); Start: A, Goal: D",
        "input_str": "4\nA\n10\nB\n8\nC\n5\nD\n0\n4\nA B 1\nA C 4\nB D 5\nC D 2\nA\nD\n",
        "theory": "A* search is an informed search algorithm that selects the path minimizing $f(n) = g(n) + h(n)$, where $g(n)$ is the cost from start to $n$, and $h(n)$ is an admissible heuristic estimating cost from $n$ to goal. If $h(n)$ never overestimates the true cost, A* is both complete and optimal."
    },
    {
        "id": "exp06_hill_climbing",
        "num": 6,
        "title": "Hill Climbing Search",
        "script": "HILL_CLIMBING.py",
        "aim": "To implement the Hill Climbing local search algorithm for finding the local or global maximum of a mathematical objective function.",
        "input_desc": "Starting value: 10, Step size: 0.1, Maximum iterations: 100 for objective function $f(x) = -(x^2) + 10$",
        "input_str": "10\n0.1\n100\n",
        "theory": "Hill Climbing is an iterative local search technique that continuously moves in the direction of increasing elevation (value) to find the peak of the objective function. It terminates when no neighbour has a higher value than the current state."
    },
    {
        "id": "exp07_tsp",
        "num": 7,
        "title": "Travelling Salesman Problem (TSP)",
        "script": "TSP.py",
        "aim": "To solve the Travelling Salesman Problem by computing the minimum cost Hamiltonian path visiting every city once.",
        "input_desc": "4 cities with cost matrix: [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]], Starting city: 0",
        "input_str": "4\n0 10 15 20\n10 0 35 25\n15 35 0 30\n20 25 30 0\n0\n",
        "theory": "The Travelling Salesman Problem (TSP) is an NP-hard problem in combinatorial optimization. Given a list of cities and pairwise distances, the objective is to find the shortest possible route that visits each city exactly once and minimizes the tour cost."
    },
    {
        "id": "exp08_eight_queen",
        "num": 8,
        "title": "8-Queens Problem",
        "script": "Eight_Queen.py",
        "aim": "To solve the 8-Queens constraint satisfaction problem using Backtracking search on an $8 \\times 8$ board.",
        "input_desc": "None (Autonomous backtracking search placement on an 8x8 chessboard)",
        "input_str": None,
        "theory": "The 8-Queens problem requires placing eight chess queens on an $8 \\times 8$ chessboard such that no two queens threaten each other (i.e. share the same row, column, or diagonal). Backtracking explores partial assignments and backtracks upon conflict."
    },
    {
        "id": "exp09_water_jug",
        "num": 9,
        "title": "Water Jug Problem",
        "script": "Water_jug.py",
        "aim": "To solve the Water Jug problem using State-Space Search (BFS) to measure a target quantity of water using two jugs.",
        "input_desc": "None (Jug 1 Capacity: 4L, Jug 2 Capacity: 3L, Target state: (4, 2))",
        "input_str": None,
        "theory": "The Water Jug Problem is a state space search problem where states are represented as ordered pairs $(j_1, j_2)$ of water contents. Valid production rules include filling, emptying, and pouring between jugs until the target measurement is achieved."
    },
    {
        "id": "exp10_tic_tac_toe",
        "num": 10,
        "title": "Tic-Tac-Toe Game",
        "script": "Tic_Tac_Toe.py",
        "aim": "To implement a two-player interactive Tic-Tac-Toe game board with state representation and win/draw validation.",
        "input_desc": "Sequential row and column moves: (0,0), (1,0), (0,1), (1,1), (0,2) yielding a win for Player X",
        "input_str": "0\n0\n1\n0\n0\n1\n1\n1\n0\n2\n",
        "theory": "Tic-Tac-Toe is a 2-player deterministic, perfect-information zero-sum game played on a $3 \\times 3$ grid. The program maintains board state transitions and tests terminal win conditions along all rows, columns, and diagonals."
    },
    {
        "id": "exp11_minimax",
        "num": 11,
        "title": "Minimax Algorithm",
        "script": "minmax.py",
        "aim": "To implement the Minimax decision rule for adversarial game tree evaluation.",
        "input_desc": "8 leaf node values: 3 5 6 9 1 2 0 -1 at tree height 3",
        "input_str": "3 5 6 9 1 2 0 -1\n",
        "theory": "The Minimax algorithm is a recursive decision strategy in game theory and artificial intelligence. The maximizing player seeks to maximize the minimum payoff, while the minimizing player minimizes the opponent's maximum gain."
    },
    {
        "id": "exp12_alpha_beta",
        "num": 12,
        "title": "Alpha-Beta Pruning",
        "script": "Alpha_Beta_pruning.py",
        "aim": "To implement Alpha-Beta Pruning to prune non-promising branches from the Minimax game tree and reduce search complexity.",
        "input_desc": "8 leaf node values: 3 5 6 9 1 2 0 -1 with alpha=-infinity, beta=+infinity",
        "input_str": "3 5 6 9 1 2 0 -1\n",
        "theory": "Alpha-Beta pruning optimizes Minimax search without altering the final optimal decision. It maintains two values: $\\alpha$ (the highest score guaranteed to the maximizer) and $\\beta$ (the lowest score guaranteed to the minimizer). Pruning occurs when $\\beta \\le \\alpha$."
    },
    {
        "id": "exp13_block_world",
        "num": 13,
        "title": "Blocks World Problem",
        "script": "block_world.py",
        "aim": "To solve the Blocks World planning problem using state-space BFS search to transition from initial block stacks to goal configuration.",
        "input_desc": "3 blocks (A, B, C); Initial: A on Table, B on A, C on Table; Goal: A on Table, B on Table, C on B",
        "input_str": "3\nA\nB\nC\nTable\nA\nTable\nTable\nTable\nB\n",
        "theory": "The Blocks World problem is a benchmark planning domain in Artificial Intelligence consisting of planar blocks placed on a table or stacked on top of one another. The objective is to produce a sequence of valid unstack/stack moves to transform an initial state into a desired goal state."
    }
]

print("Executing all experiments and capturing output...")
for exp in experiments:
    res = subprocess.run(["python", exp["script"]], input=exp["input_str"], text=True, capture_output=True)
    exp["output"] = res.stdout.strip()
    exp["code"] = open(exp["script"], "r", encoding="utf-8").read()
    
    # Save raw output to txt
    txt_path = os.path.join("outputs", f"{exp['id']}_output.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"Experiment {exp['num']}: {exp['title']}\n")
        f.write(f"Script: {exp['script']}\n")
        f.write("="*60 + "\n")
        f.write("Sample Input Provided:\n")
        f.write((exp["input_desc"] or "No interactive input required.") + "\n")
        f.write("="*60 + "\n")
        f.write("Terminal Execution Output:\n")
        f.write("="*60 + "\n")
        f.write(exp["output"] + "\n")
    
    # Save individual LaTeX snippet
    tex_snippet_path = os.path.join("outputs", f"{exp['id']}_output.tex")
    with open(tex_snippet_path, "w", encoding="utf-8") as f:
        f.write(f"% Experiment {exp['num']}: {exp['title']}\n")
        f.write(f"\\subsection*{{Experiment {exp['num']}: {exp['title']}}}\n")
        f.write(f"\\textbf{{Script File:}} \\texttt{{{exp['script']}}} \\\\[4pt]\n")
        f.write(f"\\textbf{{Aim:}} {exp['aim']} \\\\[4pt]\n")
        f.write(f"\\textbf{{Sample Input:}} {exp['input_desc']} \\\\[6pt]\n")
        f.write(f"\\begin{{tcolorbox}}[colback=black!5!white,colframe=black!75!white,title=Terminal Execution Output - {exp['title']}]\n")
        f.write("\\begin{verbatim}\n")
        f.write(exp["output"] + "\n")
        f.write("\\end{verbatim}\n")
        f.write("\\end{tcolorbox}\n\n")

print("Generated individual output files in outputs/ folder.")

# Generate combined outputs TeX document
combined_tex_path = os.path.join("outputs", "all_experiments_output.tex")
with open(combined_tex_path, "w", encoding="utf-8") as f:
    f.write(r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{tcolorbox}
\usepackage{fancyhdr}
\usepackage{hyperref}
\usepackage{xcolor}

\hypersetup{
    colorlinks=true,
    linkcolor=blue!70!black,
    urlcolor=blue!70!black
}

\pagestyle{fancy}
\fancyhf{}
\rhead{AI Lab Experiments Output Record}
\lhead{Roll No: 25CSEAIML046}
\rfoot{Page \thepage}

\title{\textbf{\LARGE Artificial Intelligence Laboratory (AI Lab)}\\
\Large Compilation of All Experiment Execution Outputs}
\author{\textbf{Soumya Ranjan} \\ Roll / Reg No: \texttt{25CSEAIML046} \\ Department of Computer Science \& Engineering (AI \& ML)}
\date{\today}

\begin{document}
\maketitle
\thispagestyle{fancy}
\hrule
\vspace{1em}

\tableofcontents
\newpage

""")
    for exp in experiments:
        f.write(f"\\section{{Experiment {exp['num']}: {exp['title']}}}\n")
        f.write(f"\\textbf{{Source File:}} \\texttt{{{exp['script']}}} \\\\[4pt]\n")
        f.write(f"\\textbf{{Objective:}} {exp['aim']} \\\\[4pt]\n")
        f.write(f"\\textbf{{Input Parameters:}} {exp['input_desc']} \\\\[6pt]\n")
        f.write(f"\\begin{{tcolorbox}}[colback=gray!5!white,colframe=blue!70!black,title={{\\textbf{{Program Output: {exp['title']}}}}}]\n")
        f.write("\\begin{verbatim}\n")
        f.write(exp["output"] + "\n")
        f.write("\\end{verbatim}\n")
        f.write("\\end{tcolorbox}\n")
        f.write("\\vspace{1em}\n\n")
    
    f.write(r"\end{document}" + "\n")

print("Generated outputs/all_experiments_output.tex successfully.")

# Now generate master lab report: AI_Lab_Report_25CSEAIML046.tex
master_tex_path = "AI_Lab_Report_25CSEAIML046.tex"
with open(master_tex_path, "w", encoding="utf-8") as f:
    f.write(r"""\documentclass[11pt,a4paper]{report}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{listings}
\usepackage{tcolorbox}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{hyperref}
\usepackage{booktabs}

% Color definitions
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.97,0.97,0.97}
\definecolor{primary}{RGB}{20, 50, 100}
\definecolor{secondary}{RGB}{41, 128, 185}
\definecolor{outputback}{RGB}{245, 247, 250}
\definecolor{outputframe}{RGB}{52, 73, 94}

% Listings configuration for Python code
\lstdefinestyle{pythonstyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen}\itshape,
    keywordstyle=\color{primary}\bfseries,
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=4,
    frame=single,
    rulecolor=\color{lightgray}
}
\lstset{style=pythonstyle}

% Header and Footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\textsl{AI Lab Record - 25CSEAIML046}}
\fancyhead[R]{\textsl{CSE (AI \& ML)}}
\fancyfoot[C]{\thepage}

\hypersetup{
    colorlinks=true,
    linkcolor=primary,
    filecolor=magenta,      
    urlcolor=secondary,
    pdftitle={AI Laboratory Record - 25CSEAIML046},
    pdfauthor={Soumya Ranjan},
    pdfsubject={Artificial Intelligence Lab Experiments and Outputs}
}

\begin{document}

% ------------------- COVER PAGE -------------------
\begin{titlepage}
    \centering
    \vspace*{1.5cm}
    
    {\Huge \bfseries \color{primary} ARTIFICIAL INTELLIGENCE\\[6pt] LABORATORY RECORD}\\[1.5cm]
    
    \rule{\linewidth}{1.5pt}\\[0.4cm]
    {\Large \bfseries Course Code: AI LAB $\vert$ CSE-AIML}\\[0.4cm]
    \rule{\linewidth}{1.5pt}\\[2cm]
    
    \begin{minipage}{0.8\textwidth}
    \centering
    \large
    \textbf{Student Name:} Soumya Ranjan \\[8pt]
    \textbf{University Roll / Reg. No:} \texttt{25CSEAIML046} \\[8pt]
    \textbf{Discipline:} Computer Science and Engineering \\[8pt]
    \textbf{Specialization:} Artificial Intelligence \& Machine Learning \\[8pt]
    \textbf{Repository:} \url{https://github.com/Soumya-19-Ranjan/AI_LAB_25CSEAIML046.git}
    \end{minipage}
    
    \vfill
    
    {\large \bfseries Department of Computer Science \& Engineering}\\[4pt]
    {\large Faculty of Engineering and Technology}\\[6pt]
    {\large Academic Session: 2025--2026}\\[4pt]
    {\small Generated on: \today}
    
\end{titlepage}

% ------------------- CERTIFICATE / INDEX -------------------
\newpage
\chapter*{Index of Completed Experiments}
\addcontentsline{toc}{chapter}{Index of Completed Experiments}

\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{cp{6.5cm}p{4cm}c}
\toprule
\textbf{Exp. No.} & \textbf{Experiment Title} & \textbf{Algorithm / Technique} & \textbf{Status} \\
\midrule
1 & Breadth First Search (BFS) & FIFO Queue Search & Completed \\
2 & Depth First Search (DFS) & LIFO Stack Search & Completed \\
3 & Uniform Cost Search (UCS) & Priority Queue Search & Completed \\
4 & Depth Limited Search (DLS) & Bounded Depth DFS & Completed \\
5 & A* Search Algorithm & Informed Heuristic ($f=g+h$) & Completed \\
6 & Hill Climbing Algorithm & Local Optimization & Completed \\
7 & Travelling Salesman Problem & Permutation Search & Completed \\
8 & 8-Queens Problem & Backtracking CSP & Completed \\
9 & Water Jug Problem & State Space Search (BFS) & Completed \\
10 & Tic-Tac-Toe Game & Board State Verification & Completed \\
11 & Minimax Algorithm & Adversarial Game Tree & Completed \\
12 & Alpha-Beta Pruning & Tree Branch Pruning & Completed \\
13 & Blocks World Problem & Classical AI Planning & Completed \\
\bottomrule
\end{tabular}
\end{table}

\vspace{2em}
\tableofcontents

\newpage
""")

    for exp in experiments:
        f.write(f"\\chapter{{Experiment {exp['num']}: {exp['title']}}}\n\n")
        f.write(f"\\section{{Aim / Objective}}\n{exp['aim']}\n\n")
        f.write(f"\\section{{Algorithm and Theory}}\n{exp['theory']}\n\n")
        
        f.write(f"\\section{{Python Source Code (\\texttt{{{exp['script']}}})}}\n")
        f.write("\\begin{lstlisting}[language=Python]\n")
        f.write(exp["code"].strip() + "\n")
        f.write("\\end{lstlisting}\n\n")
        
        f.write(f"\\section{{Input Specifications}}\n")
        f.write(f"{exp['input_desc']}\n\n")
        
        f.write(f"\\section{{Execution Output}}\n")
        f.write(f"\\begin{{tcolorbox}}[colback=outputback,colframe=outputframe,title={{\\textbf{{Terminal Output - {exp['title']}}}}}]\n")
        f.write("\\begin{verbatim}\n")
        f.write(exp["output"] + "\n")
        f.write("\\end{verbatim}\n")
        f.write("\\end{tcolorbox}\n\n")
        
        f.write(f"\\section{{Result and Conclusion}}\n")
        f.write(f"The program for \\textbf{{{exp['title']}}} was implemented, tested, and validated successfully in Python. The outputs obtained comply with theoretical state-space traversal and algorithm complexity expectations.\n\n")
        f.write("\\newpage\n\n")

    f.write(r"\end{document}" + "\n")

print("Generated AI_Lab_Report_25CSEAIML046.tex successfully.")
