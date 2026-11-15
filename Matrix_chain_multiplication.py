def matrix_chain_order(p):

    n = len(p) - 1

    # DP table for minimum multiplication cost
    dp = [[0 for _ in range(n + 1)]
          for _ in range(n + 1)]

    # Split table for optimal parenthesization
    split = [[0 for _ in range(n + 1)]
             for _ in range(n + 1)]

    # Chain length starts from 2
    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1

            dp[i][j] = float('inf')

            # Try every possible split
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


# Function to print DP table
def print_dp_table(dp, n):

    print("\n--- DP Cost Table ---")

    for i in range(1, n + 1):

        for j in range(1, n + 1):

            if i > j:
                print(" - ", end="\t")
            else:
                print(dp[i][j], end="\t")

        print()


# Main Program

n = int(input("Enter number of matrices: "))

print("\nEnter matrix dimensions.")
print("For", n, "matrices, enter", n + 1, "dimensions.")

p = list(map(int, input("Enter dimensions separated by spaces: ").split()))

if len(p) != n + 1 or any(d <= 0 for d in p):

    print("Invalid dimensions. Please enter exactly", n + 1,
          "positive integers.")

else:

    dp, split = matrix_chain_order(p)

    print_dp_table(dp, n)

    print("\nMinimum number of scalar multiplications:",
          dp[1][n])
