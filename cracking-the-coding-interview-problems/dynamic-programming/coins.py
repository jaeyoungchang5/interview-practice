#!/usr/bin/env python3

import sys

COINS = (1, 5, 10, 25)

def calculate_ways(N):
    table = [0] * (N+1+max(COINS))

    for c in COINS:
        table[c] = 1


    for i in range(1, N+1):
        for c in COINS:
            table[i+c] += 1

    print(table[N])

def main():
    for line in sys.stdin:
        N = int(line)
        calculate_ways(N)

if __name__ == '__main__':
    main()
