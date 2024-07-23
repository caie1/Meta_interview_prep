class Solution(object):
    def isStrobogrammatic(self, s):
        """
        :type num: str
        :rtype: bool
        """
       
       
        l, r =0, len(s) - 1
        
        while l <= r:
            a = int(s[l])
            b = int(s[r])
            
            if (a == 1 and b == 1) or (a == 0 and b == 0) or (a == 8 and b == 8) or (a == 6 and b == 9) or (a == 9 and b == 6):
                l += 1
                r -= 1
            else:
                return False
        return True