def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

        print("After iteration", j - p + 1, ":", A)

    A[i + 1], A[r] = A[r], A[i + 1]

    print("After Pivot: ", A)

    return i + 1

def Quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        Quick_sort(A, p, q - 1)
        Quick_sort(A, q + 1, r)

n = int(input("Enter number of elements to enter in the array: "))
A =[]

for i in range(n):
    s = int(input(f"Enter the element {i + 1}: "))
    A.append(s)

Quick_sort(A, 0, len(A) - 1)

print(A)