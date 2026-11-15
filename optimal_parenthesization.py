# Function to calculate minimum multiplication cost
def matrix_chain_order(p):

    n = len(p) - 1

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    split = [[0] * (n + 1) for _ in range(n + 1)]

    # Calculate minimum cost
    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = (
                    dp[i][k] +
                    dp[k + 1][j] +
                    p[i - 1] * p[k] * p[j]
                )

                if cost < dp[i][j]:

                    dp[i][j] = cost
                    split[i][j] = k

    return dp, split


# Function to find optimal parenthesization
def print_optimal_parenthesization(split, i, j):

    if i == j:
        return "A" + str(i)

    k = split[i][j]

    left = print_optimal_parenthesization(split, i, k)

    right = print_optimal_parenthesization(split, k + 1, j)

    return "(" + left + " x " + right + ")"


# Main Program

n = int(input("Enter number of matrices: "))

print("\nEnter", n + 1, "dimensions:")

p = list(map(int, input().split()))

if len(p) != n + 1 or any(d <= 0 for d in p):

    print("Invalid dimensions.")

else:

    dp, split = matrix_chain_order(p)

    # Display optimal parenthesization
    result = print_optimal_parenthesization(
        split, 1, n
    )

    print("\n--- Optimal Parenthesization ---")
    print(result)

    # Display minimum cost
    print("\nMinimum number of scalar multiplications:",
          dp[1][n])

    # Display split table
    print("\n--- Split Table ---")

    for i in range(1, n + 1):

        for j in range(1, n + 1):

            if i > j:
                print("-", end="\t")
            else:
                print(split[i][j], end="\t")

        print()
