class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxVal = max(nums)
        minIncrement  = 0
        freqCount = [0]*(n + maxVal + 1)
        
        for val in nums:
            freqCount[val] += 1
            
            
        for i in range(len(freqCount)):
            if freqCount[i] <= 1:
                continue
            duplicate = freqCount[i] - 1
            freqCount[i + 1] += duplicate
            freqCount[i] = 1
            minIncrement += duplicate
        return minIncrement
    
        # T(NlogN) S(N) for sorting
        nums.sort()
        count = 0
        
        for i in xrange(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                count += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return count