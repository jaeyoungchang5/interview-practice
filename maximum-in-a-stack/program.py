#!/usr/bin/env python3

'''
Maximum In A Stack:
Implement a class for a stack that supports all the regular functions (push, pop) 
and an additional function of max() which returns the maximum element in the stack (return None if the stack is empty). 
Each method should run in constant time.
'''

class MaxStack:
    def __init__(self):
        self.stack = []
        self.maximum = [0]

    def push(self, val):
        self.stack.append(val)
        if val > self.maximum[-1]:
            self.maximum.append(val)
    
    def pop(self):
        val = self.stack.pop()
        if val == self.maximum[-1]:
            self.maximum.pop()

    def max(self):
        return self.maximum[-1]


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
