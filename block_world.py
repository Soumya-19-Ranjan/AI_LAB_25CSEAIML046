from collections import deque


def is_clear(state, block):
    for b, position in state:
        if position == block:
            return False
    return True


def generate_moves(state, blocks):
    moves = []

    for block in blocks:
        if not is_clear(state, block):
            continue

        current_position = None
        for b, position in state:
            if b == block:
                current_position = position
                break

        # Move block to table
        if current_position != "Table":
            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, "Table"))

            moves.append(
                (
                    frozenset(new_state),
                    f"Move {block} from {current_position} to Table"
                )
            )

        # Move block onto another clear block
        for destination in blocks:
            if block == destination:
                continue

            if current_position == destination:
                continue

            if not is_clear(state, destination):
                continue

            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, destination))

            moves.append(
                (
                    frozenset(new_state),
                    f"Move {block} from {current_position} to {destination}"
                )
            )

    return moves


def blocks_world(initial_state, goal_state):
    queue = deque()
    queue.append((frozenset(initial_state), []))

    visited = set()
    visited.add(frozenset(initial_state))

    while queue:
        current_state, path = queue.popleft()

        if current_state == frozenset(goal_state):
            return path

        blocks = [block for block, _ in current_state]
        moves = generate_moves(current_state, blocks)

        for new_state, move in moves:
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [move]))

    return None


# ---------------- MAIN PROGRAM ----------------

print("===== BLOCK WORLD PROBLEM =====")

# Number of blocks
n = int(input("Enter number of blocks: "))

blocks = []

print("\nEnter block names:")
for i in range(n):
    block = input(f"Block {i + 1}: ")
    blocks.append(block)

# Initial state
print("\n===== INITIAL STATE =====")
print("Enter the position of each block.")
print("Enter 'Table' if the block is on the table.")

initial_state = set()

for block in blocks:
    position = input(f"Where is {block} initially? ")
    initial_state.add((block, position))

# Goal state
print("\n===== GOAL STATE =====")
print("Enter the desired position of each block.")

goal_state = set()

for block in blocks:
    position = input(f"Where should {block} be in the goal state? ")
    goal_state.add((block, position))

# Display states
print("\nInitial State:")
for block, position in initial_state:
    print(block, "->", position)

print("\nGoal State:")
for block, position in goal_state:
    print(block, "->", position)

# Solve
solution = blocks_world(initial_state, goal_state)

# Display solution
if solution:
    print("\n===== SOLUTION =====")

    for i, move in enumerate(solution, 1):
        print(f"Step {i}: {move}")

    print("\nTotal moves:", len(solution))
else:
    print("\nNo solution found.")