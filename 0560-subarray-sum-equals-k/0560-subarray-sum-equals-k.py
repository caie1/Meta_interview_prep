class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        
        curSum = 0
        count = 0
        
        for num in nums:
            curSum += num
            count += prefixSum[curSum - k]
            prefixSum[curSum] += 1
        
        return count