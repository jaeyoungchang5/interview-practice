#!/usr/bin/env python3

import sys

def count(text):
    order = []
    count = {}

    for letter in text:
        if not letter.isalpha():
            continue

        letter = letter.lower()

        if letter not in order:
            order.append(letter)

        count[letter] = count.get(letter, 0) + 1

    for letter in order:
        print(f'{letter}: {count[letter]}')

def main():
    for line in sys.stdin:
        count(line.strip())

if __name__ == '__main__':
    main()
