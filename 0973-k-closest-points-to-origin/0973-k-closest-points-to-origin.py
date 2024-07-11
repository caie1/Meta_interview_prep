class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        if k==0:
            return res
        heap=[]
        for i,l in enumerate(points):
            p=(l[0]**2)+(l[1]**2)
            heapq.heappush(heap,[p,l[0],l[1]])
        while k>0:
            p,x,y=heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res
