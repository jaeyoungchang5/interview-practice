#!/usr/bin/env python3

'''
Queue Using Two Stacks:
Implement a queue class using two stacks. 
A queue is a data structure that supports the FIFO protocol (First in = first out). 
Your class should support the enqueue and dequeue methods like a standard queue.
'''

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        front = self.queue[0]
        self.queue = self.queue[1:]
        return front

def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

if __name__ == '__main__':
    main()
