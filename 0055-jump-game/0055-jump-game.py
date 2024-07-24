class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Greedy Solution
        maxInd = 0
        
        for i in xrange(len(nums)):
            if i > maxInd:
                return False
            maxInd = max( maxInd, i + nums[i])
        
        return True
        
        