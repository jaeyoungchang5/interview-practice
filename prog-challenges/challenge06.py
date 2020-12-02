#!/usr/bin/env python3

import sys

def find_maxi(fruits):
    maxi = 0
    maxi_arr = []

    for i, fruitA in enumerate(fruits):
        seen = set()
        for j in range(i, len(fruits)):
            fruitB = fruits[j]
            if fruitB in seen:
                break

            seen.add(fruitB)

            if j-i+1 > maxi:
                maxi = j-i+1
                maxi_arr = fruits[i:j+1]

    print(f'{maxi}: {", ".join(maxi_arr)}')

def main():
    for line in sys.stdin:
        fruits = line.strip().split()
        find_maxi(fruits)

if __name__ == '__main__':
    main()
