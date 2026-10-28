# Depth Limited Search (DLS) Algorithm Implementation
# Experiment 03: Constrained Depth Backtracking Search

def dls(graph, current, goal, limit, path):
    # Record node along current exploration path
    path.append(current)

    # Goal test check
    if current == goal:
        return True

    # Depth cutoff reached - backtrack
    if limit == 0:
        path.pop()
        return False

    # Recurse on adjacent neighbors with decremented depth limit
    for neighbor in graph.get(current, []):
        if neighbor not in path:
            if dls(graph, neighbor, goal, limit - 1, path):
                return True

    # Backtrack if goal not found down this branch
    path.pop()
    return False


# ----------- Main Driver Program -----------
print("===== DEPTH LIMITED SEARCH =====")

# Input graph vertices
n = int(input("Enter number of nodes: "))
graph = {i: [] for i in range(n)}

# Input graph edges
e = int(input("Enter number of edges: "))
print("Enter edges (source destination):")

for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Input search parameters
start = int(input("Enter starting node: "))
goal = int(input("Enter goal node: "))
limit = int(input("Enter depth limit: "))
path = []

# Execute Depth Limited Search
found = dls(graph, start, goal, limit, path)

# Output traversal findings
if found:
    print("\nGoal Found!")
    print("Path:", " -> ".join(map(str, path)))
    print("Depth:", len(path) - 1)
else:
    print("\nGoal not found within the given depth limit.")
