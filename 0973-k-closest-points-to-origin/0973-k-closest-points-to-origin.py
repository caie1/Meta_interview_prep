class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        Use euclidean distance to find closest points to origin.
        Heap to store euclidean distance along with points
        Pop elements from heap until size of the heap is K
        Finally return points from heap
        N -> No. of points
        Time O(2N + KlogN + K) Space O(N)
        """
        ##Erase this solution
        '''Build max heap => pq = [2, 4] and dist 3 in this scenario, we need to pop 4'''
        pq = []
        for x, y in points:
            dist = x**2 + y**2
            if len(pq) < K:
                heapq.heappush(pq, (-dist, [x, y]))
            elif dist < -pq[0][0]:
                heapq.heappop(pq)
                heapq.heappush(pq, (-dist, [x, y]))
        result = []
        while pq:
            result.append(heapq.heappop(pq)[1])
        return result
                

        





        h = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(h, (dist, [x, y]))
        result = []
        for _ in range(K):
            result.append(heapq.heappop(h)[1])
        return result






        p = []
        for x, y in points: ##O(N)
            heapq.heappush(p, (x**2 + y**2, [x, y])) ##O(logN)
        res = []
        for i in range(K): ##O(K)
            res.append(heapq.heappop(p)[1]) ##O(logK)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         p = []
        
#         for point in points:  ##O(n)
#             val = point[0]**2 + point[1]**2
#             p.append((-val, point))  ###IMP --> max heap 
        
#         heapq.heapify(p) ##O(n)
        
#         while len(p) > K: ##O(K)
#             heapq.heappop(p)  ##O(logn)
        
#         return [point[1] for point in p] ##O(k)
    
        # points.sort(key=lambda x: x[0]**2 + x[1]**2)
        # return points[:K]
    #Time : O(NlogN)
    #Space : O(N)