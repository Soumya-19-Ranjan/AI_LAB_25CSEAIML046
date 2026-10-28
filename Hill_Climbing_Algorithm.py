# Hill Climbing Algorithm Implementation
# Experiment 06: Local Search Function Optimization

# Define the mathematical objective function to maximize
def objective_function(x):
    return -(x**2) + 10  # Parabolic curve with global peak at x = 0


# Hill climbing iterative local search
def hill_climbing(start, step_size, max_iterations):
    current = start
    current_value = objective_function(current)

    for i in range(max_iterations):
        # Generate left and right neighboring perturbations
        left = current - step_size
        right = current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        # Greedy transition to higher neighboring elevation
        if left_value > current_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:
            # Reached local peak or flat plateau - terminate search
            break

    return current, current_value


# ----------- Main Driver Program -----------
start = float(input("Enter the starting value: "))
step_size = float(input("Enter the step size: "))
max_iterations = int(input("Enter maximum iterations: "))

best_position, best_value = hill_climbing(start, step_size, max_iterations)

print("\nBest position found: ", best_position)
print("Maximum Value = ", best_value)
