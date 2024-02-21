import sys

def nearest_neighbor(graph):
    num_cities = len(graph)
    visited = [False] * num_cities
    path = [0]  # Start from the first city

    for _ in range(num_cities - 1):
        current_city = path[-1]
        min_distance = sys.maxsize
        nearest_city = None

        for neighbor in range(num_cities):
            if not visited[neighbor] and graph[current_city][neighbor] < min_distance:
                min_distance = graph[current_city][neighbor]
                nearest_city = neighbor

        visited[nearest_city] = True
        path.append(nearest_city)

    return path

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance

# Example usage:
graph_example = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp_path = nearest_neighbor(graph_example)
tsp_distance = calculate_total_distance(tsp_path, graph_example)

print("TSP Path:", tsp_path)
print("Total Distance:", tsp_distance)
