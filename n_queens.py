# Function to check whether a queen can be placed safely
def is_safe(board, row, col, n):

    for prev_col in range(col):

        prev_row = board[prev_col]

        # Check same row
        if prev_row == row:
            return False

        # Check diagonal
        if abs(prev_row - row) == abs(prev_col - col):
            return False

    return True


# Backtracking function
def solve_n_queens(board, col, n, solutions, find_all):

    # All queens are successfully placed
    if col == n:
        solutions.append(board.copy())

        if not find_all:
            return True

        return False

    # Try placing queen in every row
    for row in range(n):

        if is_safe(board, row, col, n):

            # Place queen
            board[col] = row

            # Recursive call for next column
            found = solve_n_queens(
                board, col + 1, n, solutions, find_all
            )

            # Stop after first solution
            if found:
                return True

            # Backtracking
            board[col] = -1

    return False


# Function to display chessboard
def print_board(solution, n):

    for row in range(n):

        for col in range(n):

            if solution[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# Main Program
while True:

    print("\n========== N-QUEENS PROBLEM ==========")
    print("1. Find First Solution")
    print("2. Generate All Possible Solutions")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1' or choice == '2':

        n = int(input("\nEnter number of queens (N): "))

        if n <= 0:
            print("Please enter a positive value of N.")
            continue

        board = [-1] * n
        solutions = []

        find_all = (choice == '2')

        # Calling backtracking function
        solve_n_queens(
            board, 0, n, solutions, find_all
        )

        if len(solutions) == 0:

            print("\nNo solution exists for N =", n)

        elif choice == '1':

            print("\nFirst Valid Solution:")
            print_board(solutions[0], n)

        else:

            print("\nAll Possible Solutions:")

            for index, solution in enumerate(solutions, start=1):

                print("\nSolution", index)
                print_board(solution, n)

            print("\nTotal Number of Solutions:", len(solutions))

    elif choice == '3':

        print("\nExiting N-Queens Program.")
        break

    else:

        print("\nInvalid choice! Please enter 1, 2 or 3.")
