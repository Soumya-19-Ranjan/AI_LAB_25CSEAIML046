def minmax(depth,nodeIndex, isMax, scores, height):
    if depth == height:
        return scores[nodeIndex]
    
    if isMax:
        return max(minmax(depth + 1, nodeIndex * 2, False, scores, height),
                   minmax(depth + 1, nodeIndex * 2 + 1, False, scores, height))
    else:
        return min(minmax(depth + 1, nodeIndex * 2, True, scores, height),
                   minmax(depth + 1, nodeIndex * 2 + 1, True, scores, height))

#main program
scores = list(map(int, input("Enter 8 leaf node values: ").split()))
height = 3
result = minmax(0, 0, True, scores, height)
print("The optimal value is:", result)