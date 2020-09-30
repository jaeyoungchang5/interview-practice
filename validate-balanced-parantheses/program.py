#!/usr/bin/env python3

'''
Validate Balanced Parantheses:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
'''

PARANS = {
    '}': '{',
    ')': '(',
    ']': '['
}

class Solution:
    def isValid(self, s):
        stack = []
        for paran in s:
            if paran == '{' or paran == '(' or paran == '[':
                stack.append(paran)
                continue

            if not stack:
                return 'False'
            
            top = stack.pop()
            if top != PARANS[paran]:
                return 'False'

        return 'True' if not stack else 'False'

def main():
    s = "()(){(())"
    # should return False
    print(Solution().isValid(s))

    s = ""
    # should return True
    print(Solution().isValid(s))

    s = "([{}])()"
    # should return True
    print(Solution().isValid(s))

if __name__ == '__main__':
    main()

