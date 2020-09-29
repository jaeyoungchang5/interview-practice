#!/usr/bin/env python3

'''
Find the non-duplicate number:
Given a list of numbers, where every number shows up twice except for one number, find that one number.
'''

def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result

def main():
    nums = [4, 3, 2, 4, 1, 3, 2] # result should be 2
    print(sum(nums))
    result = single_number(nums)
    print(result)

if __name__ == '__main__':
    main()
