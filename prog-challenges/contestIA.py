#!/usr/bin/env python3

import sys

def calculate_views(buildings):
    N = len(buildings) - 1

    count = 1

    for i in range(N, 0, -1):
        if buildings[i-1] > buildings[i]:
            count += 1
        else:
            break

    print(count)

def main():
    for line in sys.stdin:
        buildings = [int(b) for b in line.strip().split()]

        calculate_views(buildings)

if __name__ == '__main__':
    main()
