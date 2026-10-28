# Alpha Beta Pruning Algorithm Implementation
# Experiment 13: Branch Cutoff Optimization for Minimax Adversarial Search

import math

def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta, height):
    # Terminal leaf evaluation reached at maximum tree height
    if depth == height:
        return values[node_index]

    if maximizing_player:
        best = -math.inf
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta, height)
            best = max(best, val)
            alpha = max(alpha, best)

            # Beta cutoff: Prune branch if minimizer already has a lower bound
            if beta <= alpha:
                break
        return best

    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta, height)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha cutoff: Prune branch if maximizer already has a higher bound
            if beta <= alpha:
                break
        return best


# ----------- Main Driver Program -----------
values = list(map(int, input("Enter 8 leaf node values: ").split()))

if len(values) != 8:
    print("Please enter exactly 8 values.")
else:
    height = 3
    alpha = -math.inf
    beta = math.inf
    result = alpha_beta_pruning(0, 0, True, values, alpha, beta, height)
    print("The optimal value is: ", result)
