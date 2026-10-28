# Breadth First Search (BFS) Algorithm Implementation
# Experiment 01: Uninformed Graph Search using FIFO Queue

def bfs(graph, start_node, target_node):
    # Queue for level-by-level exploration (FIFO order)
    visited = []
    queue = [start_node]

    # Process nodes in queue
    while queue:
        current_node = queue.pop(0)

        # Explore unvisited node
        if current_node not in visited:
            print(f"Exploring node : {current_node}")
            visited.append(current_node)

            # Check if target node is reached
            if current_node == target_node:
                print(f"\nTarget node '{target_node}' found!")
                return visited

            # Enqueue unvisited adjacent neighbors
            for neighbour in graph.get(current_node, []):
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)

    print(f"\nTarget node '{target_node}' not found!")
    return visited


# ----------- User Input & Graph Setup -----------
print("------------BFS Graph Traversal with Target Search Program---------")
print("\n--------Build your graph--------")
student_graph = {}

# Read total number of edges
num_edges = int(input("\nHow many edges (connections) does your graph have : "))
print("\nEnter each edge separated by a space (e.g., A B) : ")

for i in range(num_edges):
    # Read undirected edge connections
    u, v = input(f"Edge {i+1} : ").split()

    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []

    # Add bidirectional edges
    student_graph[u].append(v)
    student_graph[v].append(u)

# Read start and target nodes
start = input("\nEnter the starting node for BFS : ")
target = input("Enter the target node : ")

print(f"\nYour graph dictionary : {student_graph}")
print("\nStarting BFS traversal.......\n")

# Execute BFS traversal
visited_nodes = bfs(student_graph, start, target)
print("\nVisited Nodes :", visited_nodes)
