from itertools import permutations

def travelling_salesman(distance):
    n = len(distance)

    # Starting city is city 0
    start = 0

    # All cities except the starting city
    cities = list(range(1, n))

    minimum_cost = float('inf')
    best_route = None

    # Generate all possible routes
    for perm in permutations(cities):

        current_city = start
        current_cost = 0
        route = [start]

        # Visit each city
        for city in perm:
            current_cost += distance[current_city][city]
            current_city = city
            route.append(city)

        # Return to starting city
        current_cost += distance[current_city][start]
        route.append(start)

        # Check whether this is the shortest route
        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_route = route

    return best_route, minimum_cost


# Distance matrix
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve TSP
route, cost = travelling_salesman(distance)

# Display result
print("Best Route:")

for city in route:
    print(chr(65 + city), end=" ")

print("\nMinimum Distance:", cost)