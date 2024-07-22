class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ##Erase this solution
        ## Time: O(N) Space: O(1)
        max_sum, cur_sum = float('-inf'), 0
        for num in nums:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
        
        ## Brute force
        max_sum = float('-inf')
        for i in range(len(nums)):
            cur_sum = 0
            for i in range(i, len(nums)):
                cur_sum += nums[i]
                max_sum = max(max_sum, cur_sum)
        return max_sum
        
        
        
        
        
        ##T(N) S(1) 
        ## Current maximum sum => What happens if we add current number to previously calculated sum or if we start new subarray from current position
        ## Compare it with our best max sub array sum
        maxsum = curmax = nums[0]
        for i in range(1, len(nums)):
            curmax = max(curmax + nums[i], nums[i])
            maxsum = max(maxsum, curmax)
        return maxsum
        ## Calculate the sum of all subarray and keep the track of best one
        ## Time: O(N^2) Space: O(1)
        maxsum = float('-inf')
        for i in range(len(nums)):
            cursum = nums[i]
            for j in range(i + 1, len(nums)):
                cursum += nums[j]
                maxsum = max(maxsum, cursum)
            if nums[i] > maxsum:
                maxsum = nums[i] ## nums = [1]
        return maxsum
    
        
        
        
        
        
        
        curMax = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            curMax = max(curMax + nums[i], nums[i])
            maxSum = max(maxSum, curMax)
        return maxSum
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        curMax = nums[0]
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            curMax = max(curMax + nums[i], nums[i]) ##[-2,-1] -1 > -3
            maxSum = max(maxSum, curMax)
        
        return maxSum
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # This solution will fail with all negative numbers 
        # max_so_far, max_ending_here = 0, 0
        # if(len(nums) == 1):
        #     max_so_far = nums[0]
        # for i in range(len(nums)):
        #     max_ending_here += nums[i]
        #     if(max_ending_here < 0):
        #         max_ending_here = 0
        #     elif(max_so_far < max_ending_here):
        #         max_so_far = max_ending_here
        # return max_so_far
        
        ##N -> len of nums Time O(N) Space O(1)
        # max_so_far = nums[0]
        # cur_max = nums[0]
        # for i in range(1, len(nums)):
        #     cur_max = max(nums[i], cur_max+nums[i]) ###Handle Negative integer [-2,-1]
        #     max_so_far = max(max_so_far, cur_max)
        # return max_so_far
        
        ###Brute Force ---> TLE
        
#         if len(nums) == 1:
#             return nums[0]
        
#         maxSum = float('-inf')
#         for i in range(len(nums)):
#             curSum = nums[i]
#             for j in range(i+1, len(nums)):
#                 curSum += nums[j]
#                 maxSum = max(maxSum, curSum)
#             if nums[i] > maxSum:
#                 maxSum = nums[i]
        
#         return maxSum