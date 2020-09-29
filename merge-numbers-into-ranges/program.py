#!/usr/bin/env python3

'''
Merge List Of Number Into Ranges:
Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.
'''

def find_ranges(nums):
    start = nums[0]
    end = nums[0]
    ranges = []
    for i in range(len(nums)):
        if nums[i] == end+1 or nums[i] == end:
            end = nums[i]
        else:
            ranges.append(str(start) + '->' + str(end))
            start = nums[i]
            end = nums[i]

    ranges.append(str(start) + '->' + str(end))

    print(ranges)

def main():
    nums = [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
    find_ranges(nums)

if __name__ == '__main__':
    main()
