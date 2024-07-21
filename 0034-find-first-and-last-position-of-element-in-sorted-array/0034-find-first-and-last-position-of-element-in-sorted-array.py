class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lowerBound = upperBound = -1
        n = len(nums)
        
        # Finding lower bound
        l, r = 0, n - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                lowerBound = mid
                r = mid - 1                
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # Finding upper bound
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                upperBound = mid
                l = mid + 1                
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return [lowerBound, upperBound]