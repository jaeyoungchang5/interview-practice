#!/usr/bin/env python3

import sys

def is_palindrome(string):
    occur = {}

    for s in string:
        occur[s] = occur.get(s, 0) + 1
    
    odds = 0
    for val in occur.values():
        odds += val % 2

    if odds <= 1:
        print('Yes')
    else:
        print('No')

def main():
    for line in sys.stdin:
        is_palindrome(line.strip())

if __name__ == '__main__':
    main()
