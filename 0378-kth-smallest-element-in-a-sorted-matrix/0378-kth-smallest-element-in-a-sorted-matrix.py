class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Binary Search Optimization
        # Get Rank Function T:O(n)
        # Main binary search T: O(max - min)
        # Overall T: O(max - min)*O(n)
        def getRank(num):
            row, col = len(matrix) - 1, 0
            rank = 0
            
            while row >= 0 and col < len(matrix[0]):
                
                if matrix[row][col] <= num:
                    rank += row + 1
                    col += 1
                else:
                    row -= 1
            return rank
        
        
        l, r = matrix[0][0], matrix[-1][-1]
        
        while l <= r:
            mid = (l + r) // 2
            
            if getRank(mid) < k:
                l = mid + 1
            else:
                r = mid - 1
        return l
        
        
        
        # Heap solution T: O(n2logk) S:O(k)
        heap = []
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                heapq.heappush(heap, -matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return - heap[0]