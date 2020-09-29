#!/usr/bin/env python3

'''
Merge Overlapping Intervals:
You are given an array of intervals - that is, an array of tuples (start, end). 
The array may not be sorted, and could contain overlapping intervals. 
Return another array where the overlapping intervals are merged.
'''

def merge_intervals(intervals):
    ranges = [(0,0)]

    for interval in intervals:
        if interval[0] > ranges[-1][1]:
            ranges.append(interval)
        else:
            for i in range(len(ranges)):
                if interval[0] < ranges[i][0] and interval[1] > ranges[i][1]:
                    ranges[i] = interval
    
    return ranges[1:]

        

def main():
    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    result = merge_intervals(intervals)

    solution_array = [(1, 3), (4, 10), (20, 25)]

    print(f'result:     {result}')
    print(f'solution:   {solution_array}')

if __name__ == '__main__':
    main()
