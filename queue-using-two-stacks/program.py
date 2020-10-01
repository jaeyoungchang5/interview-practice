#!/usr/bin/env python3

'''
Queue Using Two Stacks:
Implement a queue class using two stacks. 
A queue is a data structure that supports the FIFO protocol (First in = first out). 
Your class should support the enqueue and dequeue methods like a standard queue.
'''

class Queue:
    def __init__(self):
        self.stack = []
        self.queue = []

    def print_queue(self):
        text = []
        for i in range(len(self.queue)-1,-1,-1):
            text.append(str(self.queue[i]))
        print(f'Queue: {"->".join(text)}')

    def enqueue(self, val):
        self.stack.append(val)
        self.queue = []
        for i in range(len(self.stack)-1, -1, -1):
            self.queue.append(
                self.stack[i]
            )
        print(f'Queued: {val}')
        self.print_queue()
        print()

    def dequeue(self):
        if not self.queue:
            return "Empty"

        popped = self.queue.pop()
        self.stack = []
        for i in range(len(self.queue)-1, -1, -1):
            self.stack.append(
                self.queue[i]
            )
        print(f'Dequeued: {str(popped)}')
        self.print_queue()
        print()


def main():
    q = Queue()
    q.enqueue(3)
    q.enqueue(5)
    q.dequeue()
    q.enqueue(1)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(4)
    q.enqueue(2)
    q.dequeue()
    q.enqueue(4)
    q.enqueue(7)
    q.dequeue()
    q.dequeue()

if __name__ == '__main__':
    main()
