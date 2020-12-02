#!/usr/bin/env python3

import sys

def find_maxi(array):
    table = {0:0}
    maxi = 0
    total = 0

    for i, num in enumerate(array, 1):
        total += 1 if num == 1 else -1

        if total in table:
            maxi = max(maxi, i - table[total])
        else:
            table[total] = i

    print(maxi)

def main():
    for line in sys.stdin:
        array = map(int, line.strip().split())
        find_maxi(array)

if __name__ == '__main__':
    main()
