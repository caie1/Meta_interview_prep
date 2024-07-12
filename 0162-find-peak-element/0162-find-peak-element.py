class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
            
        l = 1
        r = len(nums) - 2
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]: # We are in increasing sequence
                l = mid + 1
            else: # We are in decreasing sequence
                r = mid - 1