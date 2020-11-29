#!/usr/bin/env python3

import sys

def collatz_iterative(n, hist):
    print(hist)
    sequence = list()
    count = 1
    while n != 1:
        if n in hist:
            count += hist[n]
            break

        if n%2 == 1:
            n = 3*n + 1
        else:
            n = n/2
        sequence.append(n)
        count += 1
    print(count)

def main():
    hist = dict()
    for line in sys.stdin:
        n = int(line)
        collatz_iterative(n, hist)

if __name__ == '__main__':
    main()
