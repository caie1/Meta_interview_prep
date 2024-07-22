class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x and x < 0:
            return False
        p = str(x)[::-1]
        
        return p == str(x)