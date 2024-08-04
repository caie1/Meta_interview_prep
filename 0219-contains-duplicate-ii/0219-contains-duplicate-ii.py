class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numMap = {}
        
        for i, v in enumerate(nums):
            if v in numMap:
                if i - numMap[v] <= k:
                    return True
            numMap[v] = i
        return False
        