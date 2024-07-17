class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ##T(NlogN) S(N)
        ##Length of heap represents no. of meeting rooms we required
        '''
        Initital heap
        sort intervals by start time
        for each start and end interval:
            if len of heap > 0 and start >= earliest end time in heap:
                then pop earliest end time
            insert current end to heap
        return len of heap
        '''
        ## Erase this solution, Time: O(2NlogN) Space: O(N)
        intervals.sort(key=lambda x:x[0])
        pq = []
        for start, end in intervals:
            if not pq or start < pq[0]:
                heapq.heappush(pq, end)
            else:
                heapq.heappop(pq)
                heapq.heappush(pq, end)
        return len(pq)
        
    
