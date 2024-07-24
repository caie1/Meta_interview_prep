class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = float("-inf")
        minPrice = float("inf")
        
        for i in xrange(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            maxProfit = max(maxProfit, (prices[i] - minPrice))
        return maxProfit