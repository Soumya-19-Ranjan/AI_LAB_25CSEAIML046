import math
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):
    if depth==height:
        return values[nodeIndex]

    if maximizingPlayer:
        maxEval = -math.inf
        for i in range(2):
           value = alpha_beta(depth+1, nodeIndex*2+i, False, values, alpha, beta, height)
           best = max(best,value)
           alpha = max(alpha, best)
           
           if beta <= alpha:
               break
        return best
    else:
        minEval = math.inf
        for i in range(2):
            value = alpha_beta(depth+1, nodeIndex*2+i, True, values, alpha, beta, height)
            best = min(best,value)
            beta = min(beta, best)
            
            if beta <= alpha:
                break
        return best

#Main Program
values = list(map(int, input("Enter 8 leaf node values: ").strip().split()))
height = 3
result = alpha_beta(0, 0, True, values, -math.inf, math.inf, height)
print("\nOptimal value:", result)