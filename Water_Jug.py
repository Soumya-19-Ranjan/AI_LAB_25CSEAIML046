# Water Jug Problem Solver using BFS
# Experiment 07: State-Space Production Rules and Breadth-First Search

from collections import deque

def water_jug(cap1, cap2, target_state):
    # Track visited states to prevent cycles: (jug1_water, jug2_water)
    visited = set()
    queue = deque()

    # Queue stores: (jug1_level, jug2_level, path_history)
    queue.append((0, 0, []))

    while queue:
        j1, j2, path = queue.popleft()

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        current_path = path + [(j1, j2)]

        # Check if destination state has been achieved
        if (j1, j2) == target_state:
            return current_path

        # Generate all 6 production rule transitions:
        next_moves = [
            (cap1, j2),                                            # 1. Fill jug 1
            (j1, cap2),                                            # 2. Fill jug 2
            (0, j2),                                               # 3. Empty jug 1
            (j1, 0),                                               # 4. Empty jug 2
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),    # 5. Pour jug 1 -> jug 2
            (j1 + min(cap1 - j1, j2), j2 - min(cap1 - j1, j2)),    # 6. Pour jug 2 -> jug 1
        ]

        # Enqueue legal and non-visited state moves
        for move in next_moves:
            if 0 <= move[0] <= cap1 and 0 <= move[1] <= cap2 and move not in visited:
                queue.append((move[0], move[1], current_path))

    return None


# ----------- Main Driver Program -----------
# Solve for Jug 1 capacity = 4L, Jug 2 capacity = 3L, Target state = (2, 3)
target_state = (2, 3)
solution = water_jug(4, 3, target_state)

if solution:
    print(f"Steps to reach the target state {target_state}:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
