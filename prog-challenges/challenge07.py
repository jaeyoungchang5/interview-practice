#!/usr/bin/env python3

import sys
import itertools

DIGITS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

def calculate(pairs):
    for p in itertools.permutations('0123456789',10):
        num1 = int(''.join(p[0:5]))
        num2 = int(''.join(p[5:10]))
        
        N = num2/num1

        if N in pairs:
            pairs[N].append([num2, num1])

def main():
    pairs = {}
    N_arr = []
    for line in sys.stdin:
        N = int(line)

        if not 2 <= N <= 100:
            break
        
        pairs[N] = []
        
    calculate(pairs)
    
    for N, solutions in pairs.items():
        if not solutions:
            print(f'There are no solutions for {N}')

        for pair in solutions:
            print(f'{pair[0]} / {pair[1]} = {N}')


if __name__ == '__main__':
    main()
