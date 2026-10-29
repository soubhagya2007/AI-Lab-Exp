from collections import deque

def water_jug(capacity_a, capacity_b, target):
    queue = deque()
    visited = set()
    parent = {}

    # Initial state
    start = (0, 0)
    queue.append(start)
    visited.add(start)
    parent[start] = None

    while queue:
        current = queue.popleft()
        a, b = current

        # Check whether target is reached
        if a == target or b == target:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Solution path:")
            for state in path:
                print(state)

            return

        # Generate possible states

        # 1. Fill Jug A
        states = [
            (capacity_a, b),

            # 2. Fill Jug B
            (a, capacity_b),

            # 3. Empty Jug A
            (0, b),

            # 4. Empty Jug B
            (a, 0)
        ]

        # 5. Pour A -> B
        amount = min(a, capacity_b - b)
        states.append((a - amount, b + amount))

        # 6. Pour B -> A
        amount = min(b, capacity_a - a)
        states.append((a + amount, b - amount))

        # Add new states to queue
        for new_state in states:
            if new_state not in visited:
                visited.add(new_state)
                parent[new_state] = current
                queue.append(new_state)

    print("No solution exists.")


# Main program
capacity_a = 4
capacity_b = 3
target = 2

water_jug(capacity_a, capacity_b, target)
