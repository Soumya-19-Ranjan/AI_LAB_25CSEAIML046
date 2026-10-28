# Minimax Algorithm Implementation
# Experiment 12: Adversarial Search in Two-Player Zero-Sum Game Tree

def minimax(depth, node_index, is_max, scores, height):
    # Terminal leaf evaluation reached at tree height
    if depth == height:
        return scores[node_index]

    # Maximizing player's perspective
    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height),
        )
    # Minimizing player's perspective
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height),
        )


# ----------- Main Driver Program -----------
scores = list(map(int, input("Enter 8 leaf node values: ").split()))

if len(scores) != 8:
    print("Please enter exactly 8 values.")
else:
    height = 3
    result = minimax(0, 0, True, scores, height)
    print("\nThe optimal value is: ", result)

