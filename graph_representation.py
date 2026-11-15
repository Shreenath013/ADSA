vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

# Initializing adjacency matrix
adj_matrix = [[0 for _ in range(vertices + 1)]
              for _ in range(vertices + 1)]

# Initializing adjacency list
adj_list = {i: [] for i in range(1, vertices + 1)}

print("\nEnter edges (source destination):")

for _ in range(edges):
    u, v = map(int, input().split())

    # Updating adjacency matrix
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1

    # Updating adjacency list
    adj_list[u].append(v)
    adj_list[v].append(u)


# Displaying adjacency matrix
print("\n--- Adjacency Matrix ---")

print("  ", end="")
for i in range(1, vertices + 1):
    print(i, end=" ")
print()

for i in range(1, vertices + 1):
    print(i, end=" ")
    for j in range(1, vertices + 1):
        print(adj_matrix[i][j], end=" ")
    print()


# Displaying adjacency list
print("\n--- Adjacency List ---")

for vertex in adj_list:
    print(vertex, "->", adj_list[vertex])
