#!/usr/bin/env python3

import sys

def check_tags(line):
    i = 0
    stack = list() # LIFO approach with stack
    while i < len(line):
        if line[i] == '<':
            tag = ''
            i += 1

            # if closing bracket
            if line[i] == '/':
                i += 1
                while i < len(line):
                    if line[i] == '>':
                        break
                    tag += line[i]
                    i += 1
                if tag == stack[-1]:
                    stack.pop()
                else:
                    return False
                continue

            # store tag in stack
            while i < len(line):
                if line[i] == '>':
                    break
                tag += line[i]
                i += 1
            stack.append(tag)

        i += 1
    if not stack:
        return True
    else:
        return False


def main():
    for line in sys.stdin:
        is_balanced = check_tags(line)

        print('Balanced' if is_balanced else 'Unbalanced')


if __name__ == '__main__':
    main()
