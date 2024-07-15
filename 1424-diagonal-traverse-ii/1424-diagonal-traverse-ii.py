class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        """
        Diagonal elements have same sum of their row, col indices
        Use deque because we are traversing righmost elements first
        Time O(m*n) Space O(N)
        """
        
        cellMap = defaultdict(deque)
        
        for i in xrange(len(nums)):
            for j in xrange(len(nums[i])):
                cellMap[i+j].appendleft(nums[i][j])
        res = []
        for val in cellMap.values():
            res.extend(val)
        return res
        
        