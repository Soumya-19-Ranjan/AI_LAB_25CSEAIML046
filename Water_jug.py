from collections import deque
from importlib.resources import path

def water_jug(cap1, cap2, target_state):
    visited = set()
    queue = deque()  # Start with both jugs empty
    queue.append((0, 0, []))  # (jug1, jug2, path)
    while queue:
        j1, j2, path = queue.popleft()  

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        current_path = path + [(j1, j2)]

        if (j1, j2) == target_state:
            return current_path

        next_moves = [
            (cap1, j2),  # Fill jug1
            (j1, cap2),  # Fill jug2
            (0, j2),     # Empty jug1
            (j1, 0),     # Empty jug2
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),  # Pour jug1 to jug2
            (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1))   # Pour jug2 to jug1
        ]
        for move in next_moves:
            if move not in visited:
                queue.append((move[0], move[1], current_path))

    return None  # No solution found

target_goal = (4,2)
solution = water_jug(4, 3, target_goal)

if solution:
    print(f"steps to reach the target state {target_goal}:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
