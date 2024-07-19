class Solution(object):
            
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Gap method tabulation with higher space usage (very important)
        n = len(s)
        dp = [[False]*n for _ in xrange(n)]
        count = 0
    
        for gap in xrange(n):
            for i in xrange(n - gap):
                j = i + gap
                
                if gap == 0:
                    dp[i][j] = True
                elif gap == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                if dp[i][j]:
                    count += 1
        
        return count
            
