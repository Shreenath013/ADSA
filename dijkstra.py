import heapq

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

choice = input("Enter graph type (D for Directed, U for Undirected): ").upper()

# Creating adjacency list
graph = {i: [] for i in range(1, vertices + 1)}

print("\nEnter edges (source destination weight):")

for _ in range(edges):
    u, v, w = map(int, input().split())

    if w < 0:
        print("Error: Dijkstra's algorithm does not support negative weights.")
        exit()

    graph[u].append((v, w))

    if choice == 'U':
        graph[v].append((u, w))


# Dijkstra function
def dijkstra(graph, vertices, source):

    # Initialize distances
    distance = [float('inf')] * (vertices + 1)

    distance[source] = 0

    # Priority queue
    pq = [(0, source)]

    while pq:

        dist, vertex = heapq.heappop(pq)

        # Skip outdated entries
        if dist > distance[vertex]:
            continue

        # Visit adjacent vertices
        for neighbour, weight in graph[vertex]:

            new_distance = dist + weight

            if new_distance < distance[neighbour]:

                distance[neighbour] = new_distance

                heapq.heappush(
                    pq, (new_distance, neighbour)
                )

    return distance


# Taking source vertex
source = int(input("\nEnter source vertex: "))

# Calling Dijkstra algorithm
distances = dijkstra(graph, vertices, source)

# Displaying shortest distances
print("\n--- Dijkstra's Shortest Path Results ---")
print("Source Vertex:", source)

for i in range(1, vertices + 1):

    if distances[i] == float('inf'):
        print(f"Vertex {i}: Unreachable")
    else:
        print(f"Vertex {i}: {distances[i]}")
