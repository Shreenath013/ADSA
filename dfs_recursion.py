def dfs(graph, vertex, visited):

    # Mark current vertex as visited
    visited[vertex] = True

    # Print visited vertex
    print(vertex, end=" ")

    # Visit all adjacent unvisited vertices
    for neighbour in graph[vertex]:

        if not visited[neighbour]:
            dfs(graph, neighbour, visited)


# Main Program

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

# Visited array (1-based indexing)
visited = [False] * (vertices + 1)

# Displaying DFS traversal
print("\nDFS Traversal:")

dfs(graph, start, visited)

print()
