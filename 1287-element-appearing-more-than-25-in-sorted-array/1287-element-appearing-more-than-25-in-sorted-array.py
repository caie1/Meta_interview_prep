class Solution(object):
    def findSpecialInteger(self, nums):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        count = 1
        threshold = len(nums) // 4
        
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count > threshold:
                    return nums[i]
 