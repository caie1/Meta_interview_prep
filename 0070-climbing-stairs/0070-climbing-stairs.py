class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
                #Tabulation
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in xrange(1,n+1):
            oneJump = dp[i - 1]
            twoJump = 0
            if i > 1:
                twoJump = dp[i - 2]
            dp[i] = oneJump + twoJump
        return dp[n]
    
        # Memoization
        memo = {0:1}
        def helper(m):
            if m < 0:
                return 0
            if m in memo:
                return memo[m]
            oneJump = helper(m - 1)
            TwoJump = helper(m - 2)
            memo[m] = oneJump + TwoJump
            return memo[m]
        return helper(n)
    
