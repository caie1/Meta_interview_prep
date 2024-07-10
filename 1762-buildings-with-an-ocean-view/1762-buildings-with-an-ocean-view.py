class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        res = [n - 1]
        
        for i in xrange(n-2, -1, -1):
            if heights[i] > heights[res[-1]]:
                res.append(i)
                
        return res[::-1]