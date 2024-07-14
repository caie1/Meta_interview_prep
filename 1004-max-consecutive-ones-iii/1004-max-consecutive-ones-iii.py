class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        countZero = 0
        maxLen = 0
        
        l = r = 0
        
        while r < len(nums):
            if nums[r] == 0:
                countZero += 1
            
            if countZero <= k:
                maxLen = max(maxLen, (r - l + 1))
            
            else:
                while countZero > k:
                    if nums[l] == 0:
                        countZero -= 1
                    l += 1
            r += 1
        
        return maxLen