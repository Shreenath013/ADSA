import heapq

# Taking graph details
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

# Creating adjacency list
graph = {i: [] for i in range(1, vertices + 1)}

print("\nEnter edges (source destination weight):")

for _ in range(edges):
    u, v, w = map(int, input().split())

    # Undirected graph
    graph[u].append((v, w))
    graph[v].append((u, w))


# Prim's Algorithm
def prims_mst(graph, vertices, start):

    visited = set()
    mst = []
    total_weight = 0

    # Priority queue: (weight, source, destination)
    pq = [(0, -1, start)]

    while pq and len(visited) < vertices:

        weight, u, v = heapq.heappop(pq)

        if v in visited:
            continue

        visited.add(v)

        # Ignore the starting vertex's dummy edge
        if u != -1:
            mst.append((u, v, weight))
            total_weight += weight

        # Add adjacent edges
        for neighbour, edge_weight in graph[v]:

            if neighbour not in visited:
                heapq.heappush(
                    pq, (edge_weight, v, neighbour)
                )

    return mst, total_weight, visited


# Main program
start = int(input("\nEnter starting vertex: "))

mst, total_weight, visited = prims_mst(
    graph, vertices, start
)

# Display MST
print("\n--- Prim's Minimum Spanning Tree ---")

if len(visited) != vertices:
    print("Graph is disconnected. A complete MST does not exist.")
    print("Minimum Spanning Forest edges:")

for u, v, weight in mst:
    print(f"{u} -- {v} : {weight}")

print("Total MST Weight:", total_weight)
