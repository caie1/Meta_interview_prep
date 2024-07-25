class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        n = 1
        maxNum = max(nums)
        while n <= maxNum:
            if n not in numSet:
                return n
            n += 1
        return n
