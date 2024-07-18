class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charMap = set()
        
        for c in s:
            if c in charMap:
                charMap.remove(c)
            else:
                charMap.add(c)
            
        return True if 0 <= len(charMap) <= 1 else False
        