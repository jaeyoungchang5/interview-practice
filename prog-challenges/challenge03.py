#!/usr/bin/env python3

import sys
from math import inf

def search(arr, target):
    if not arr:
        return inf
    midpoint = len(arr)//2
    mid = arr[midpoint]
    left = arr[0]
    right = arr[-1]

    if mid == target:
        return midpoint

    # shifted right; right is sorted
    if mid < left:
        if target > mid and target <= right:
            return search(arr[midpoint+1:], target) + midpoint + 1
        else:
            return search(arr[:midpoint], target)

    # shifted left; left is sorted
    else:
        if target < mid and target >= left:
            return search(arr[:midpoint], target)
        else:
            return search(arr[midpoint+1:], target) + midpoint + 1


def main():
    for line in sys.stdin:
        arr = list(map(int, line.split()))
        target = int(sys.stdin.readline().strip())
        index = search(arr, target)
        if index != inf:
            print(f'{target} found at index {index}')
        else:
            print(f'{target} was not found')

if __name__ == '__main__':
    main()
