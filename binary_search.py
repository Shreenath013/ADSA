# Iterative Approach
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1


# Recursive Approach
def binary_search_recursive(arr, low, high, target):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return binary_search_recursive(arr, low, mid - 1, target)

    else:
        return binary_search_recursive(arr, mid + 1, high, target)


arr = list(map(int, input("Enter sorted array elements: ").split()))

target = int(input("Enter element to search: "))

print("\nArray:", arr)
print("Target Element:", target)

# Iterative Search
result1 = binary_search_iterative(arr, target)

print("\n--- Iterative Binary Search ---")

if result1 != -1:
    print("Element found at index:", result1)
    print("Position:", result1 + 1)
else:
    print("Element not found")


# Recursive Search
result2 = binary_search_recursive(arr, 0, len(arr) - 1, target)

print("\n--- Recursive Binary Search ---")

if result2 != -1:
    print("Element found at index:", result2)
    print("Position:", result2 + 1)
else:
    print("Element not found")
