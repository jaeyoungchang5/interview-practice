#!/bin/python3

import sys

''' Question:

Implement a stack that accepts the following commands and performs the operations described:
- push v: push int v onto the top of the stack
- pop: pop the top element from the stack
- inc i v: add v to the bottom i elements in stack

Additionally, the stack should support the following functions:
- empty: return True if stack is empty, false if not
- peek: return the top element of the stack
- sum: return the sum of all the elements

ALL OPERATIONS MUST RUN IN AMORTIZED O(1) TIME
==> very tricky for the inc i v command
'''

class AddingStack:
    def __init__(self) -> None:
        self.stack = []
        self.sum_stack = 0
        self.index = -1

    def push(self, v: int) -> None:
        self.stack.append(v)
        self.index += 1
        self.sum_stack += v

    def pop(self) -> None:
        popped_value = self.stack.pop()
        self.sum_stack -= popped_value
        self.index -= 1

    def inc(self, i: int, v: int) -> None:
        self.sum_stack += i*v

        for ind in range(i):
            self.stack[ind] += v

    def empty(self) -> bool:
        if self.index < 0:
            return True
        else:
            return False

    def peek(self) -> int:
        return self.stack[self.index]

    def sum(self) -> int:
        return self.sum_stack


if __name__ == "__main__":
    operations_cnt = 0
    operations_cnt = int(input())
    operations_i = 0
    stack = AddingStack()
    while operations_i < operations_cnt:
        try:
            operation = str(input())
        except:
            continue
        operations_i += 1

        commands = operation.split()
        if commands[0] == "push":
            stack.push(int(commands[1]))
        elif commands[0] == "pop":
            stack.pop()
        elif commands[0] == "inc":
            stack.inc(int(commands[1]), int(commands[2]))

        if stack.empty():
            print("EMPTY")
        else:
            print(stack.peek(), stack.sum())
