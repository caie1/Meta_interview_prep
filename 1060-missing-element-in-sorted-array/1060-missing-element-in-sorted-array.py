class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        missingNums = [0]*n
        missingNums[0] = 0
        
        for i in xrange(1,n):
            missingNums[i] = nums[i] - (nums[i - 1] + 1) + missingNums[i - 1]
        
        if k > missingNums[-1]:
            return nums[-1] + (k - missingNums[-1])
        
        l, r = 0, n - 1
        
        while l <= r:
            mid = (l + r)//2
            
            if missingNums[mid] >= k:
                r = mid - 1
            else:
                l = mid + 1
        
        return nums[r] + (k - missingNums[r])