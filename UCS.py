# Uniform Cost Search (UCS) Algorithm Implementation
# Experiment 04: Optimal Path Search using Priority Queue

import heapq

def ucs(graph, start, goal):
    # Priority Queue stores tuples of: (cumulative_cost, current_node, path)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    # Dictionary to keep track of lowest cost found for each visited node
    visited = {}

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        # Skip node if a cheaper path has already been processed
        if current in visited and visited[current] <= cost:
            continue

        visited[current] = cost

        # Goal test check
        if current == goal:
            return path, cost

        # Relax and enqueue neighboring edges with cumulative cost
        for neighbor, edge_cost in graph.get(current, []):
            new_cost = cost + edge_cost
            new_path = path + [neighbor]
            heapq.heappush(priority_queue, (new_cost, neighbor, new_path))

    return None, float("inf")


# ----------- Main Driver Program -----------
print("===== UNIFORM COST SEARCH =====")

# Input vertices and edges
n = int(input("Enter number of nodes: "))
graph = {i: [] for i in range(n)}

e = int(input("Enter number of edges: "))
print("Enter edges as:")
print("source destination cost")

for i in range(e):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

# Input query endpoints
start = int(input("Enter starting node: "))
goal = int(input("Enter goal node: "))

# Execute Uniform Cost Search
path, cost = ucs(graph, start, goal)

# Display optimal path results
if path:
    print("\nGoal Found!")
    print("Optimal Path:", " -> ".join(map(str, path)))
    print("Minimum Cost:", cost)
else:
    print("\nGoal not found.")
