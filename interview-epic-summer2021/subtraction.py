#!/usr/bin/env python3

import sys

def long_subtract(num1_array, num2_array):
    N = len(num1_array)

    add_on = [0] * (N-len(num2_array))
    num2_array = add_on + num2_array

    borrow = False

    result = [0] * N

    for i in range(N-1, -1, -1):
        num1 = num1_array[i]
        num2 = num2_array[i]
        if borrow:
            num1 -= 1

        if num1 < num2:
            result[i] = (num1+10)-num2
            borrow = True
        else:
            result[i] = num1-num2
            borrow = False

    final = []
    for num in result:
        if num == 0:
            continue

        final.append(num)

    is_positive = final[0] > 0

    return final, is_positive

def main():
    for line in sys.stdin:
        num1 = [int(num) for num in line.strip().split()]

        num2 = [int(num) for num in sys.stdin.readline().strip().split()]
        
        final, is_positive = long_subtract(num1, num2)
        print(final)
        print('Positive' if is_positive else 'Negative')

if __name__ == '__main__':
    main()
