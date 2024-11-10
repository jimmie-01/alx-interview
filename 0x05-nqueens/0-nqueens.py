#!/usr/bin/python3
"""Module N-queens"""

import sys

def is_safe(board, row, col, N):
    # Check column on this row
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(N, 0, board, solutions)
    return solutions

def solve_nqueens_util(N, row, board, solutions):
    if row == N:
        solutions.append([[i, row] for i, cell in enumerate(board[row]) if cell == 1])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(N, row + 1, board, solutions)
            board[row][col] = 0

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
