class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = j = k = -1
        
        for ind, v in enumerate(nums):
            if i == -1 or nums[ind] <= nums[i]:
                i = ind
            elif j == -1 or nums[ind] <= nums[j]:
                j = ind
            elif k == -1:
                return True
        return False