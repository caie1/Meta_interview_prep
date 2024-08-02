class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(str):
            l, r = 0, len(str) - 1
            while l < r:
                if str[l] != str[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res= []
        
        def helper(ind, path):
            # Base Case
            if ind == len(s):
                res.append(path)
                return None

            for i in xrange(ind, len(s)):
                if isPalindrome(s[ind:i + 1]):
                    helper(i + 1, path + [s[ind:i + 1]])
        helper(0,[])
        return res