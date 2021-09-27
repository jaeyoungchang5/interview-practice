#!/bin/python3

import math
import os
import random
import re
import sys

''' Question

Given a chess board of n rows (top to bottom) and n columns (left to right)
In each move, a knight moves either:
- 2 col and 1 row
- 2 row and 1 col

A bishop moves any number of steps diagonally

Both the knight and bishop capture any piece that is on a position that it moves to.
A position that a piece can move to is said to be threatened by that piece, 
because if another piece moves to that position, then it can be caputred.

Given a starting position A and ending position B for the knight, and a bishop position C, 
calculate the minimum number of moves needed by the knight to move from A to B while avoiding all 
positions threated by the bishop.

If the knight caputers the bishop on one of its moves, then it can move into positions that were previously threatened by the bishop.

If there is no possible path to B, return -1.

Knight can move to bishop ending position even if it is threatened

'''

#
# Complete the 'moves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER startRow
#  3. INTEGER startCol
#  4. INTEGER endRow
#  5. INTEGER endCol
#  6. INTEGER bishopRow
#  7. INTEGER bishopCol

from math import inf

# build a table of spaces the knight CANNOT move to


def find_invalid_spaces(n, row, col):
    # initialize table to all True
    can_move = [([True] * (n)) for _ in range(n)]

    # mark diagonals of bishop as FALSE (check params)
    for i in range(n):
        if row + i < n and col + i < n:
            can_move[row+i][col+i] = False

        if row - i >= 0 and col - i >= 0:
            can_move[row-i][col-i] = False

        if row+i < n and col-i >= 0:
            can_move[row+i][col-i] = False

        if row-i >= 0 and col+i < n:
            can_move[row-i][col+i] = False

    # return table
    return can_move

# fill board


def fill_board(board, i, j, can_move, bishop_alive=True, hunt_bishop=False):
    # first check if arg is in bounds
    # then check if bishop is alive
    # - if bishop is alive and you can kill it, then kill it and start computing min
    # - if bishop is alive, then make sure can_move[row][col] == True, and THEN compute min
    # - if bishop is dead, then compute min

    # (row-1, col-2), (row+1, col-2)
    if hunt_bishop is True and bishop_alive and i-1 == bishopRow and j-2 == bishopCol:
        bishop_alive = False
        board[i-1][j-2] = min(board[i][j]+1, board[i-1][j-2])
    if i-1 >= 0 and j-2 >= 0 and ((bishop_alive and can_move[i-1][j-2]) or not bishop_alive):
        board[i-1][j-2] = min(board[i][j]+1, board[i-1][j-2])
    if hunt_bishop is True and bishop_alive and i+1 == bishopRow and j-2 == bishopCol:
        bishop_alive = False
        board[i+1][j-2] = min(board[i][j]+1, board[i+1][j-2])
    if i+1 < n and j-2 >= 0 and ((bishop_alive and can_move[i+1][j-2]) or not bishop_alive):
        board[i+1][j-2] = min(board[i][j]+1, board[i+1][j-2])

    # (row-1, col+2), (row+1, col+2)
    if hunt_bishop is True and bishop_alive and i-1 == bishopRow and j+2 == bishopCol:
        bishop_alive = False
        board[i-1][j+2] = min(board[i][j]+1, board[i-1][j+2])
    if i-1 >= 0 and j+2 < n and ((bishop_alive and can_move[i-1][j+2]) or not bishop_alive):
        board[i-1][j+2] = min(board[i][j]+1, board[i-1][j+2])
    if hunt_bishop is True and bishop_alive and i+1 == bishopRow and j+2 == bishopCol:
        bishop_alive = False
        board[i+1][j+2] = min(board[i][j]+1, board[i+1][j+2])
    if i+1 < n and j+2 < n and ((bishop_alive and can_move[i+1][j+2]) or not bishop_alive):
        board[i+1][j+2] = min(board[i][j]+1, board[i+1][j+2])

    # (row+2, col-1), (row+2, col+1)
    if hunt_bishop is True and bishop_alive and i+2 == bishopRow and j-1 == bishopCol:
        bishop_alive = False
        board[i+2][j-1] = min(board[i][j]+1, board[i+2][j-1])
    if i+2 < n and j-1 >= 0 and ((bishop_alive and can_move[i+2][j-1]) or not bishop_alive):
        board[i+2][j-1] = min(board[i][j]+1, board[i+2][j-1])
    if hunt_bishop is True and bishop_alive and i+2 == bishopRow and j+1 == bishopCol:
        bishop_alive = False
        board[i+2][j+1] = min(board[i][j]+1, board[i+2][j+1])
    if i+2 < n and j+1 < n and ((bishop_alive and can_move[i+2][j+1]) or not bishop_alive):
        board[i+2][j+1] = min(board[i][j]+1, board[i+2][j+1])

    # (row-2, col-1), (row-2, col+1)
    if hunt_bishop is True and bishop_alive and i-2 == bishopRow and j-1 == bishopCol:
        bishop_alive = False
        board[i-2][j-1] = min(board[i][j]+1, board[i-2][j-1])
    if i-2 >= 0 and j-1 >= 0 and ((bishop_alive and can_move[i-2][j-1]) or not bishop_alive):
        board[i-2][j-1] = min(board[i][j]+1, board[i-2][j-1])
    if hunt_bishop is True and bishop_alive and i-2 == bishopRow and j+1 == bishopCol:
        bishop_alive = False
        board[i-2][j+1] = min(board[i][j]+1, board[i-2][j+1])
    if i-2 >= 0 and j+1 < n and ((bishop_alive and can_move[i-2][j+1]) or not bishop_alive):
        board[i-2][j+1] = min(board[i][j]+1, board[i-2][j+1])

    return board, bishop_alive

# determine min moves it will take


def moves(n, startRow, startCol, endRow, endCol, bishopRow, bishopCol):
    # get board of moves we can make if bishop is alive
    can_move = find_invalid_spaces(n, bishopRow, bishopCol)
    can_move[bishopRow][bishopCol] = True # knight can move to end pos even if threated

    # initialize board to inf
    board = [[inf]*(n) for _ in range(n)]

    board[startRow][startCol] = 0
    # copy board into hunt_board to see what the min moves is when you kill the bishop
    hunt_board = board

    # ASSUME YOU DON'T KILL BISHOP
    # iterate through board and fill board starting from start position
    for i in range(startRow, n):
        for j in range(startCol, n):
            board, bishop_alive = fill_board(board, i, j, can_move)

    # iterate through board and fill board from beginning again
    for i in range(n):
        for j in range(n):
            board, bishop_alive = fill_board(board, i, j, can_move)

    # ASSUME YOU DO KILL BISHOP IF POSSIBLE
    # bool to check if bishop is alive
    bishop_alive = True
    # iterate through board and fill board starting from start position
    for i in range(startRow, n):
        for j in range(startCol, n):
            hunt_board, bishop_alive = fill_board(
                hunt_board, i, j, can_move, bishop_alive, hunt_bishop=True)
    # iterate through board and fill board from beginning again
    for i in range(n):
        for j in range(n):
            hunt_board, bishop_alive = fill_board(
                hunt_board, i, j, can_move, bishop_alive, hunt_bishop=True)

    for row in board:
        print(row)
    print()
    min_moves = min(board[endRow][endCol], board[endRow][endCol])
    return min_moves if min_moves != inf else -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    startRow = int(input().strip())

    startCol = int(input().strip())

    endRow = int(input().strip())

    endCol = int(input().strip())

    bishopRow = int(input().strip())

    bishopCol = int(input().strip())

    result = moves(n, startRow, startCol, endRow, endCol, bishopRow, bishopCol)

    fptr.write(str(result) + '\n')

    fptr.close()
