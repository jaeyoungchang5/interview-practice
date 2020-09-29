#!/usr/bin/env python3

class MaxStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        self.stack.pop()

    def max(self):
        maximum = 0
        for element in self.stack:
            if element > maximum:
                maximum = element
        return maximum


def main():
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    print(s.max()) # 3
    s.pop()
    s.pop()
    print(s.max()) # 2

if __name__ == '__main__':
    main()