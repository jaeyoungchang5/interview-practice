#!/usr/bin/env python3

import sys
import itertools

DIALS = {
    0: '46',
    1: '68',
    2: '79',
    3: '48',
    4: '039',
    5: '',
    6: '017',
    7: '26',
    8: '13',
    9: '24'
}

def calculate_hops(curr, num, cache={}):
    if num == 1:
        return 1

    pair = (curr, num)

    if pair not in cache:
        cache[pair] = sum(calculate_hops(int(n), num-1, cache) for n in DIALS[curr])

    return cache[pair]

def main():
    for line in sys.stdin:
        start, hops = line.strip().split()

        print(calculate_hops(int(start), int(hops)))

if __name__ == '__main__':
    main()
