class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Greedy Solution
        maxSoFar = 0
        n = len(nums)
        i = 0
        
        while i < n:
            maxSoFar = max(maxSoFar, i + nums[i])
            if maxSoFar >= n - 1:
                return True
            i += 1
            if i > maxSoFar:
                return False
        
        