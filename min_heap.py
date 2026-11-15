n = int(input("Enter number of elements: "))
heap = [0] * n

# Insertion
for i in range(n):
    heap[i] = int(input(f"Enter Element {i + 1}: "))

    j = i

    # Heapify Up
    while j > 0:
        parent = (j - 1) // 2

        if heap[parent] <= heap[j]:
            break

        heap[parent], heap[j] = heap[j], heap[parent]
        j = parent

print("\nMin-Heap (BFS / Level Order):")
for i in range(n):
    print(heap[i], end=" ")


# Extract-Min
minimum = heap[0]
heap[0] = heap[n - 1]
n = n - 1

# Heapify Down
i = 0

while True:
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i

    if left < n and heap[left] < heap[smallest]:
        smallest = left

    if right < n and heap[right] < heap[smallest]:
        smallest = right

    if smallest == i:
        break

    heap[i], heap[smallest] = heap[smallest], heap[i]
    i = smallest


print("\n\nExtracted Minimum:", minimum)

print("\nHeap after Extract-Min (BFS):")
for i in range(n):
    print(heap[i], end=" ")