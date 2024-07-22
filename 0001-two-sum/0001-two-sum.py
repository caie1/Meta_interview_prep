class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        
        for i in xrange(len(nums)):
            reqNum = target - nums[i]
            if reqNum in numMap:
                return [i, numMap[reqNum]]
            numMap[nums[i]] = i