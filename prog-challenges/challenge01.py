#!/usr/bin/env python3

import sys
from math import inf

def occurences(s1, s2):
    occur = dict()
    for letter in s1:
        if letter not in occur:
            occur[letter] = 1
            continue

        occur[letter] += 1
    
    min_occur = inf
    for letter in s2:
        if occur[letter] < min_occur:
            min_occur = occur[letter]

    print(min_occur)

def main():
    for line in sys.stdin:
        s1, s2 = line.split()
        occurences(s1, s2)

if __name__ == '__main__':
    main()
