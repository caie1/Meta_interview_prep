class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = []
        dp.append([1])
        for i in xrange(1, numRows):
            level = []
            for j in xrange(i + 1):
                a = b = 0
                if j <= i - 1:
                    a = dp[i - 1][j]
                if j > 0:
                    b = dp[i - 1][j - 1]
                level.append(a + b)
            dp.append(level)
        return dp