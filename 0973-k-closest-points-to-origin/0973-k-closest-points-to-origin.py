class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
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
