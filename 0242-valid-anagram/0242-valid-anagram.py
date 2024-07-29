class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        charMap = [0]*26
        
        for i in xrange(len(s)):
            indS = ord(s[i]) - ord("a")
            indt = ord(t[i]) - ord("a")
            charMap[indS] += 1
            charMap[indt] -= 1
        
        return True if max(charMap) == 0 else False
        
        