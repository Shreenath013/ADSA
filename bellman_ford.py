vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

choice = input("Enter graph type (D for Directed, U for Undirected): ").upper()

# Creating edge list
edges = []

print("\nEnter edges (source destination weight):")

for _ in range(edges_count):
    u, v, w = map(int, input().split())

    edges.append((u, v, w))

    # For undirected graph, add reverse edge
    if choice == 'U':
        edges.append((v, u, w))


# Bellman-Ford function
def bellman_ford(vertices, edges, source):

    # Initialize distances
    distance = [float('inf')] * (vertices + 1)

    distance[source] = 0

    # Relax all edges V-1 times
    for _ in range(vertices - 1):

        updated = False

        for u, v, weight in edges:

            if distance[u] != float('inf'):

                new_distance = distance[u] + weight

                if new_distance < distance[v]:

                    distance[v] = new_distance
                    updated = True

        # Stop early if no distance changes
        if not updated:
            break

    # Check for negative-weight cycle
    for u, v, weight in edges:

        if (distance[u] != float('inf') and
                distance[u] + weight < distance[v]):

            return None

    return distance


# Taking source vertex
source = int(input("\nEnter source vertex: "))

# Calling Bellman-Ford algorithm
distances = bellman_ford(vertices, edges, source)

# Displaying results
print("\n--- Bellman-Ford Shortest Path Results ---")
print("Source Vertex:", source)

if distances is None:

    print("Negative weight cycle detected!")
    print("Shortest paths cannot be determined.")

else:

    for i in range(1, vertices + 1):

        if distances[i] == float('inf'):
            print(f"Vertex {i}: Unreachable")
        else:
            print(f"Vertex {i}: {distances[i]}")
