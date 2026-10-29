import heapq

# Graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 3)],
    'C': [('A', 4), ('D', 1)],
    'D': [('B', 3), ('C', 1), ('E', 2)],
    'E': [('D', 2)]
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 2,
    'E': 0
}


def a_star(graph, heuristic, start, goal):

    # Priority queue
    open_list = []

    # g(start) = 0
    heapq.heappush(
        open_list,
        (heuristic[start], start)
    )

    # Cost from start
    g_cost = {start: 0}

    # Store parent nodes
    parent = {start: None}

    while open_list:

        # Node with smallest f(n)
        f_current, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path, g_cost[goal]

        # Explore neighbors
        for neighbor, cost in graph[current]:

            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                # Update cost
                g_cost[neighbor] = new_g

                # Calculate f(n)
                f_neighbor = new_g + heuristic[neighbor]

                # Add to priority queue
                heapq.heappush(
                    open_list,
                    (f_neighbor, neighbor)
                )

                # Store parent
                parent[neighbor] = current

    return None, float("inf")


# Run A*
path, cost = a_star(
    graph,
    heuristic,
    'A',
    'E'
)

print("Shortest Path:", path)
print("Total Cost:", cost)