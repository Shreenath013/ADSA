vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

# Creating adjacency list (1-based indexing)
graph = {i: [] for i in range(1, vertices + 1)}

print("\nEnter edges (source destination):")

for _ in range(edges):
    u, v = map(int, input().split())

    # Adding edges (Undirected Graph)
    graph[u].append(v)
    graph[v].append(u)


# Taking starting vertex
start = int(input("\nEnter starting vertex: "))

# Initializing visited array
visited = [False] * (vertices + 1)

# Initializing explicit stack
stack = [start]

# DFS Traversal
print("\nDFS Traversal:")

while stack:

    # Remove the top element from stack
    vertex = stack.pop()

    # Check whether vertex is visited
    if not visited[vertex]:

        # Mark vertex as visited
        visited[vertex] = True

        # Print current vertex
        print(vertex, end=" ")

        # Push adjacent unvisited vertices
        for neighbour in reversed(graph[vertex]):

            if not visited[neighbour]:
                stack.append(neighbour)

print()
