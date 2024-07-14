class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        ## Start with a thinking of counter and determining gaps and thinking about edge case when arr doesn't start with lower or doesn't end with upper 
        ## How to determine missing range? Take example of 0, 2 ==> 0 + 1 <= 2 - 1 if true then found missing range. 
        ## Time: O(N) Space: O(1)
        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            cur = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= cur - 1:
                result.append([prev + 1, cur - 1])
            prev = cur
        return result



