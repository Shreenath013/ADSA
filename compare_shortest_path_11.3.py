import heapq
import time


# Dijkstra's Algorithm
def dijkstra(vertices, graph, source):

    distance = [float('inf')] * (vertices + 1)
    distance[source] = 0

    pq = [(0, source)]

    while pq:

        dist, vertex = heapq.heappop(pq)

        if dist > distance[vertex]:
            continue

        for neighbour, weight in graph[vertex]:

            new_distance = dist + weight

            if new_distance < distance[neighbour]:

                distance[neighbour] = new_distance

                heapq.heappush(
                    pq, (new_distance, neighbour)
                )

    return distance


# Bellman-Ford Algorithm
def bellman_ford(vertices, edges, source):

    distance = [float('inf')] * (vertices + 1)
    distance[source] = 0

    for _ in range(vertices - 1):

        updated = False

        for u, v, weight in edges:

            if distance[u] != float('inf'):

                new_distance = distance[u] + weight

                if new_distance < distance[v]:

                    distance[v] = new_distance
                    updated = True

        if not updated:
            break

    # Negative cycle detection
    for u, v, weight in edges:

        if (distance[u] != float('inf') and
                distance[u] + weight < distance[v]):

            return None

    return distance


# Main Program
vertices = int(input("Enter number of vertices: "))
edge_count = int(input("Enter number of edges: "))

choice = input(
    "Enter graph type (D for Directed, U for Undirected): "
).upper()

graph = {i: [] for i in range(1, vertices + 1)}
edges = []

print("\nEnter edges (source destination weight):")

for _ in range(edge_count):

    u, v, w = map(int, input().split())

    edges.append((u, v, w))
    graph[u].append((v, w))

    if choice == 'U':
        edges.append((v, u, w))
        graph[v].append((u, w))


source = int(input("\nEnter source vertex: "))

negative_weights = any(w < 0 for u, v, w in edges)


# Running Bellman-Ford
start_time = time.perf_counter()

bf_result = bellman_ford(vertices, edges, source)

bf_time = time.perf_counter() - start_time


# Running Dijkstra only if weights are non-negative
if not negative_weights:

    start_time = time.perf_counter()

    d_result = dijkstra(vertices, graph, source)

    d_time = time.perf_counter() - start_time

else:
    d_result = None
    d_time = None


# Displaying comparison
print("\n========== COMPARATIVE ANALYSIS ==========")

print("\n--- Dijkstra's Algorithm ---")

if negative_weights:
    print("Cannot be applied: Negative edge weights found.")

else:
    for i in range(1, vertices + 1):

        if d_result[i] == float('inf'):
            print(f"Vertex {i}: Unreachable")
        else:
            print(f"Vertex {i}: {d_result[i]}")

    print("Execution Time:", f"{d_time:.8f}", "seconds")


print("\n--- Bellman-Ford Algorithm ---")

if bf_result is None:

    print("Negative weight cycle detected!")
    print("Shortest paths cannot be determined.")

else:

    for i in range(1, vertices + 1):

        if bf_result[i] == float('inf'):
            print(f"Vertex {i}: Unreachable")
        else:
            print(f"Vertex {i}: {bf_result[i]}")

    print("Execution Time:", f"{bf_time:.8f}", "seconds")


print("\n--- Performance Comparison ---")

if not negative_weights and bf_result is not None:

    print("Dijkstra Time:", f"{d_time:.8f}", "seconds")
    print("Bellman-Ford Time:", f"{bf_time:.8f}", "seconds")

    if d_time < bf_time:
        print("Dijkstra was faster for this execution.")
    elif bf_time < d_time:
        print("Bellman-Ford was faster for this execution.")
    else:
        print("Both took approximately equal time.")

elif negative_weights:

    print("Dijkstra is not suitable for this graph.")
    print("Bellman-Ford supports negative edge weights.")
