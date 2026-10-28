# Traveling Salesman Problem (TSP) Implementation
# Experiment 09: Minimum Hamiltonian Tour using Exhaustive Permutations

from itertools import permutations

def travelling_salesman(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)
    min_cost = float("inf")
    best_path = None

    # Evaluate every candidate permutation of remaining cities
    for perm in permutations(cities):
        current_cost = 0
        current_path = [start]
        k = start

        # Sum distances between consecutive cities
        for city in perm:
            current_cost += graph[k][city]
            current_path.append(city)
            k = city

        # Add cost to return back to start city (complete tour)
        current_cost += graph[k][start]
        current_path.append(start)

        # Track global minimum tour cost
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return min_cost, best_path


# ----------- Main Driver Program -----------
n = int(input("Enter the number of cities: "))
print("Enter the cost matrix (space-separated values for each row):")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting city (0 to {}): ".format(n - 1)))
cost, path = travelling_salesman(graph, start)

print("\nOptimal path:", " -> ".join(map(str, path)))
print("Minimum cost:", cost)
