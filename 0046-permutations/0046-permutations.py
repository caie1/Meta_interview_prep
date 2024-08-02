class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numMap = defaultdict(int)
        res = []
        n = len(nums)
        
        def helper(path):
            #Base Case
            if len(path) == n:
                res.append(path)
                return
            
            for num in nums:
                if num not in numMap:
                    numMap[num] = 1
                    helper(path + [num])
                    del numMap[num]
        helper([])
        return res