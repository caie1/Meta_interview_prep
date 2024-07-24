class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # There are two checks; one for odd length substring and one for even length substring
        res = ""
        resLen = -1
        
        for i in  xrange(len(s)):
                    
            # For odd length substring
            l = r = i
            while l >= 0 and r < len(s) and (s[l] == s[r]):
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                l -= 1
                r += 1
                        
            # For even length substring
            l, r = i, i + 1
            while l >=0 and r < len(s) and (s[l] == s[r]):
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                l -= 1
                r += 1
            
        return res