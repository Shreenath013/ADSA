n = int(input("Enter number of elements: "))


# Initializing parent and rank arrays
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)


# Find operation with Path Compression
def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


# Union operation with Union by Rank
def union(x, y):

    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        print("Both elements belong to the same set.")
        return

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y

    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x

    else:
        parent[root_y] = root_x
        rank[root_x] += 1

    print("Union successful.")


# Display operation
def display_sets():

    sets = {}

    for i in range(1, n + 1):

        root = find(i)

        if root not in sets:
            sets[root] = []

        sets[root].append(i)

    print("\nCurrent Disjoint Sets:")

    for root, elements in sets.items():
        print("Set:", elements)


# Main Menu
while True:

    print("\n--- Disjoint Set Operations ---")
    print("1. Find")
    print("2. Union")
    print("3. Display Sets")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        x = int(input("Enter element: "))

        if 1 <= x <= n:
            print("Representative of", x, "is:", find(x))
        else:
            print("Invalid element.")

    elif choice == 2:

        x = int(input("Enter first element: "))
        y = int(input("Enter second element: "))

        if 1 <= x <= n and 1 <= y <= n:
            union(x, y)
        else:
            print("Invalid element.")

    elif choice == 3:

        display_sets()

    elif choice == 4:

        print("Exiting Disjoint Set program.")
        break

    else:
        print("Invalid choice. Try again.")
