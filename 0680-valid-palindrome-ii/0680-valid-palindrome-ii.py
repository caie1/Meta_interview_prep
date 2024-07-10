class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrom(l,r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrom(l, r - 1) or isPalindrom(l + 1, r)
        return True