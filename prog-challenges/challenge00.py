#!/usr/bin/env python3

import sys

def read_matrix(N):
    matrix = []
    for _ in range(N):
        matrix.append([int(num) for num in sys.stdin.readline().split()])
    return matrix

def rotate_matrix(matrix, N):
    final = ''
    for i in range(N):
        for row in reversed(matrix):
            final += str(row[i]) + ' '
        final = final.strip() + '\n'
    print(final)

def main():
    for line in sys.stdin:
        N = int(line)
        if N == 0:
            break
        matrix = read_matrix(N)
        rotate_matrix(matrix, N)

if __name__ == '__main__':
    main()
