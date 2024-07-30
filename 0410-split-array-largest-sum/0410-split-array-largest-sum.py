class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        Intuition Behind the Solution :- 
        The goal of this problem is to split the array nums into k or fewer subarrays such that the largest sum among           these subarrays is minimized. The function uses binary search to efficiently find this minimum possible largest         sum.

        Steps and Explanation
        Define the Binary Search Range:

        The smallest possible value for the largest sum is the maximum element in nums (since no subarray can have a sum         smaller than the largest individual element).
        The largest possible value for the largest sum is the sum of all elements in nums (if there were only one               subarray).
        
        """
        def possible(largest):
            curSum = 0
            count = 0
            for n in nums:
                curSum += n
                if (curSum > largest) and count < k:
                    curSum = n
                    count += 1 # (*)
            return (curSum <= largest) and (count + 1 <= k) # At (*) we start adding count to 1 only after we look for second subarray; basically counting one less at the end 
        
        l = max(nums)
        res = r = sum(nums)
        
        while l <= r:
            mid = l + ((r - l) // 2) # Avoid Overflow due to sum of nums
            
            if possible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res