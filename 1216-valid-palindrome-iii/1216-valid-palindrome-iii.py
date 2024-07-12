class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        memo = {}
        def helper(l, r, k):
            if k < 0:
                return False
            if l == r:
                return True
            if (l, r, k) in memo:
                return memo[(l, r, k)]
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    memo[(l, r, k)] = helper(l + 1, r, k - 1) or helper(l, r - 1, k - 1)
                    return memo[(l, r, k)]
            return True
        
        return helper(l, r, k)