class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def backtrack(i, j):
            if j == len(p):
                return i == len(s)
            if (i, j) in memo:
                return memo[(i, j)]
            firstMatch = i < len(s) and (s[i] == p[j] or p[j] == '?')
            if j < len(p) and p[j] == '*':
                res = backtrack(i, j + 1) or i < len(s) and backtrack(i + 1, j)
            else:
                res = firstMatch and backtrack(i + 1, j + 1)
            memo[(i, j)] = res
            return memo[(i, j)]
        return backtrack(0, 0)
        
        
        
        