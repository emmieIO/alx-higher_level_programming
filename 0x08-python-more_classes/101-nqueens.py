#!/usr/bin/python
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at a given position on the board.

    Args:
        board (list[list[int]]): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.
        N (int): The size of the chessboard (N × N).

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check the column on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    """
    Solve the N queens puzzle and print all solutions.

    Args:
        N (int): The number of queens and the size of the chessboard (N × N).
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solve_nqueens_helper(board, 0, N)

def solve_nqueens_helper(board, col, N):
    """
    Helper function to recursively solve the N queens puzzle.

    Args:
        board (list[list[int]]): The current state of the chessboard.
        col (int): The current column being considered.
        N (int): The size of the chessboard (N × N).

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_helper(board, col + 1, N) or res
            board[i][col] = 0

    return res

def print_solution(board):
    """
    Print a single solution to the N queens puzzle.

    Args:
        board (list[list[int]]): The current state of the chessboard.
    """
    for row in board:
        print(" ".join(map(str, row)))

def main():
    """
    Main function to handle command-line arguments and start the program.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)

if __name__ == "__main__":
    main()

