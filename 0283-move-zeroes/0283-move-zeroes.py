class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        
        
        
        
        l = 0 
        while l < len(nums) and nums[l] != 0:
            l += 1
        if l == len(nums):
            return 
        r = l + 1
        
        while r < len(nums):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            while r < len(nums) and nums[r] == 0:
                r += 1
    
                
                
        
        