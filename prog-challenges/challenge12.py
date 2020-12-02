#!/usr/bin/env python3

import sys
from math import inf

def read_grid(N):
    grid = [[0] * (N+1)]
    for _ in range(N):
        grid.append([0]+ list(map(int, sys.stdin.readline().strip().split())))

    return grid

def kakamora(grid, table, N):
    for row in range(1, N+1):
        for col in range(1, N+1):
            table[row][col] = grid[row][col] + min(
                table[row][col-1],
                table[row-1][col],
                table[row-1][col-1],
            )
    
    return table[N][N]

def reconstruct_path(grid, table, N):
    row, col = N, N
    path = []

    while row > 0 and col > 0:
        path.append(grid[row][col])
        if table[row][col] - grid[row][col] == table[row][col-1]:
            col -= 1
        elif table[row][col] - grid[row][col] == table[row-1][col]:
            row -= 1
        else:
            col -= 1
            row -= 1

    path = reversed(path)
    return list(path)

def main():
    for line in sys.stdin:
        N = int(line)
        
        # read in grid
        grid = read_grid(N)

        # initialize table
        table = [[0] + [inf for _ in range(N)] ]
        for _ in range(N):
            table.append([inf for _ in range(N+1)])

        # calculate path length
        path_length = kakamora(grid, table, N)

        # reconstruct path
        path = reconstruct_path(grid, table, N)

        # print results
        print(path_length)
        print(path)

if __name__ == '__main__':
    main()
