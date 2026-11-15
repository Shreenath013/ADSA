n = int(input("Enter number of elements: "))
heap = [0] * n

# Insertion
for i in range(n):
    heap[i] = int(input(f"Enter Element {i + 1}: "))

    j = i

    # Heapify Up
    while j > 0:
        parent = (j - 1) // 2

        if heap[parent] >= heap[j]:
            break

        heap[parent], heap[j] = heap[j], heap[parent]
        j = parent

print("\nMax-Heap (BFS / Level Order):")
for i in range(n):
    print(heap[i], end=" ")


# Extract-Max
maximum = heap[0]
heap[0] = heap[n - 1]
n = n - 1

# Heapify Down
i = 0

while True:
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and heap[left] > heap[largest]:
        largest = left

    if right < n and heap[right] > heap[largest]:
        largest = right

    if largest == i:
        break

    heap[i], heap[largest] = heap[largest], heap[i]
    i = largest


print("\n\nExtracted Maximum:", maximum)

print("\nHeap after Extract-Max (BFS):")
for i in range(n):
    print(heap[i], end=" ")