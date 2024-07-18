class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #total number of integers between [nums[0], nums[i]] is A = nums[i] - nums[0] + 1
        # Total number of existing elements is B = i + 1
        # Total number of missing elements til nums[i] is A - B = nums[i] - nums[0] + 1 - (i + 1)
        
        n = len(nums)
        left, right = 0, n - 1
        
        while left < right:
            mid = right - (right - left) // 2
            if (nums[mid] - nums[0]) - mid < k:
                left = mid
            else:
                right = mid - 1
        """
        The answer, the \U0001d458\U0001d461ℎ missing element must be somewhere to the right of nums[left]. There will         be no elements in the array between the answer and nums[left]. We don't know the answer yet,         but let's focus on the range [nums[0], answer]. We know that it contains left + 1 elements           from the input array, and k missing elements (by definition, the last element of the range           answer is the \U0001d458\U0001d461ℎ missing element). Therefore the total number of elements in the range is:           elements from the input + missing elements = left + 1 + k. Finally, as we know, answer -             nums[0] + 1 is the size of the range. Setting these equations equal to each other, we can             rearrange for answer.
        answer - nums[0] + 1 = left + 1 + k -> answer = nums[0] + left + k
        
        """
        
        return nums[0] + left + k
        
        # Time complexity O(n + logn) Space complexity O(n) 
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