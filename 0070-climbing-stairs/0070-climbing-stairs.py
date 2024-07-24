class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
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