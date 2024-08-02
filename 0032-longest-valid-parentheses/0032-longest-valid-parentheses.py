class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        Initialize your stack with -1. -1 will help you to calculate length of valid parentheses staring from 0 index. Traverse on the given string and if '(' push it to stack. If you see ')' then pop from stack. In case stack empty then push current index to stack as this is going to be the starting point to calculate longest length other wise compute the length of valid parentheses and compare against previously stored result.
        T(N) S(N)
        '''
        
        stack = [-1]
        maxLen = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, (i - stack[-1]))
        return maxLen