#!/usr/bin/env python3

import sys

HAPPY = dict()

def is_happy(num, seen):
    if num in seen:
        return False
    if num == 1:
        return True

    seen.add(num)

    if num not in HAPPY:
        new = sum([int(x) * int(x) for x in str(num)])
        HAPPY[num] = is_happy(new, seen)

    return HAPPY[num]

def main():
    for line in sys.stdin:
        num = int(line.strip())

        print('Yes' if is_happy(num, set()) else 'No')
        # print(HAPPY)

if __name__ == '__main__':
    main()
