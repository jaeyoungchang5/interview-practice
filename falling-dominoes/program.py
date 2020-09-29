#!/usr/bin/env python3

'''
Falling Dominoes:
Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still
L represents that the domino is falling to the left side
R represents that the domino is falling to the right side

Figure out the final position of the dominoes. 
If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.
'''

class Solution(object):
    def push_dominoes(self, dominoes):
        solution = list(dominoes)
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                # if i == len(dominoes):
                #     solution[i] = '.'
                #     continue
                solution[i+1] = 'R'
            elif dominoes[i] == 'L':
                if i == 0:
                    solution[i] = '.'
                    continue
                solution[i-1] = 'L'
                
        return ''.join(solution)


def main():
    print('..R...L..R.')
    solution = Solution().push_dominoes('L.R...L..R.')
    print(solution)
    print('..RR.LL..RR')

if __name__ == '__main__':
    main()
