class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Heap solution T: O(n2logk) S:O(k)
        heap = []
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                heapq.heappush(heap, -matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return - heap[0]