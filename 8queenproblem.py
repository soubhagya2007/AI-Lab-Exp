# Program to solve the 8-Queens Problem using Backtracking

N = 8

# Create an N x N chessboard
board = [["." for _ in range(N)] for _ in range(N)]


# Function to check whether a queen can be placed
def is_safe(row, col):

    # Check the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


# Backtracking function
def solve_queens(row):

    # All queens have been placed
    if row == N:
        return True

    # Try every column in the current row
    for col in range(N):

        # Check whether position is safe
        if is_safe(row, col):

            # Place queen
            board[row][col] = "Q"

            # Recursively place queen in next row
            if solve_queens(row + 1):
                return True

            # Backtrack: remove queen
            board[row][col] = "."

    return False


# Solve the problem
if solve_queens(0):

    print("Solution for 8-Queens Problem:")

    for row in board:
        print(" ".join(row))

else:
    print("No solution exists.")