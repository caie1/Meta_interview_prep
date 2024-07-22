import math

class Solution(object):
    
    def __init__(self):
        self.k = 0
        self.heap = []
        
    def kHeap(self, num):
        heapq.heappush(self.heap, - num) # Max heap structure
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Optimal Solution
        """
        While figuring divisors, we have some small divisor multplied with big divisor so only scan till 
        sqrt(n) + 1
        """
        self.k = k
        
        for num in xrange(1, int(math.sqrt(n)) + 1):
            if n % num == 0:
                self.kHeap(num)
                if num != (n // num):
                    self.kHeap(n // num)
                    
        return - self.heap[0] if len(self.heap) == self.k else -1
        
        # Brute Force Solution
#         count = 1
        
#         for num in xrange(1, n + 1):
#             if n % num == 0:
#                 if count == k:
#                     return num
#                 count += 1
#         return - 1