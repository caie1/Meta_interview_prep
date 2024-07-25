class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        pos = 0
        r = 0
        while r < n and pos < n:
            while (r < n) and (nums[r] == val):
                r += 1
            if r == n:
                break
            nums[pos] = nums[r]
            pos += 1
            r += 1
        return pos