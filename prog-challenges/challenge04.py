#!/usr/bin/env python3

import sys

ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
suits = ('C', 'D', 'H', 'S')

class Person:
    def __init__(self, name, rank, suit):
        self.name = name
        self.rank = rank
        self.suit = suit

def sort(people):
    people = sorted(people, key=lambda x:suits.index(x.suit), reverse=True)
    people = sorted(people, key=lambda x:ranks.index(x.rank), reverse=True)
    final_order = ''
    for i, person in enumerate(people):
        if i == len(people)-1:
            final_order += person.name
            continue

        final_order += person.name + ', '

    print(final_order)

def main():
    for line in sys.stdin:
        N = int(line)

        if N == 0:
            break

        people = []
        for _ in range(N):
            name, rank, suit = sys.stdin.readline().split()
            people.append(Person(name, rank, suit))
        sort(people)

if __name__ == '__main__':
    main()
