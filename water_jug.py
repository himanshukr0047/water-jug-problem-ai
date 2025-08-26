from collections import deque

def water_jug_problem(jug1, jug2, target):
    # Queue for BFS
    visited = set()
    queue = deque([(0, 0)])  # (jug1_water, jug2_water)

    while queue:
        x, y = queue.popleft()

        # If target found
        if x == target or y == target:
            print("Solution found: Jug1 =", x, "Jug2 =", y)
            return True

        # If already visited, skip
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Possible states
        next_states = [
            (jug1, y),          # Fill Jug1
            (x, jug2),          # Fill Jug2
            (0, y),             # Empty Jug1
            (x, 0),             # Empty Jug2
            (x - min(x, jug2-y), y + min(x, jug2-y)),  # Pour Jug1 -> Jug2
            (x + min(y, jug1-x), y - min(y, jug1-x))   # Pour Jug2 -> Jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("No solution possible")
    return False

# Example run
water_jug_problem(4, 3, 2)
