class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numMap = set()
        
        for num in nums:
            if num in numMap:
                return True
            numMap.add(num)
        return False
            