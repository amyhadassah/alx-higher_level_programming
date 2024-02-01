#!/usr/bin/python3
import sys


def print_solution(board):
    """Prints one of the possible solutions."""
    solution = []
    for row in board:
        position = []
        for col in range(len(board)):
            if row[col] == 1:
                position.append(col)
        solution.append(position)
    print(solution)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col].
    This function checks only left side for attacking queens.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    """Use backtracking to find all solutions."""
    # base case: If all queens are placed, then return True
    if col >= len(board):
        print_solution(board)
        return True

    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1
            # Make result true if any placement is possible
            res = solve_n_queens(board, col + 1) or res
            # If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
            board[i][col] = 0  # BACKTRACK
    return res


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0):
        print("No solution exists")


if __name__ == "__main__":
    main()
