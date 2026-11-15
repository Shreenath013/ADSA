vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

# Creating edge list
edges = []

print("\nEnter edges (source destination weight):")

for _ in range(edges_count):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))


# Sorting edges by weight
edges.sort()


# Disjoint Set / Union-Find
parent = [i for i in range(vertices + 1)]
rank = [0] * (vertices + 1)


# Find operation with Path Compression
def find(vertex):

    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])

    return parent[vertex]


# Union operation with Rank
def union(u, v):

    root_u = find(u)
    root_v = find(v)

    if root_u == root_v:
        return False

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v

    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u

    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


# Kruskal's Algorithm
mst = []
total_weight = 0

for weight, u, v in edges:

    if union(u, v):

        mst.append((u, v, weight))
        total_weight += weight

    if len(mst) == vertices - 1:
        break


# Display MST
print("\n--- Kruskal's Minimum Spanning Tree ---")

if len(mst) != vertices - 1:
    print("Graph is disconnected. A complete MST does not exist.")
    print("Minimum Spanning Forest edges:")

for u, v, weight in mst:
    print(f"{u} -- {v} : {weight}")

print("Total MST Weight:", total_weight)
