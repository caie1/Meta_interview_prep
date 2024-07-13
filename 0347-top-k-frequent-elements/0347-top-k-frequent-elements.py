class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''
        Store frequency in dictionary. Make a use of min heap of size k. Traverse on dictionary, if current freq of num > than lowest freq of num in heap then perform heappop and push current num with its freq to heap.
        At any point of time, heap will contain k maximum element
        T(NLogK) S(N + k)
        '''
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        h = []
        for num, f in freq.items():
            if len(h) < k:
                heapq.heappush(h, (f, num))
            elif h[0][0] < f:
                heapq.heappop(h)
                heapq.heappush(h, (f, num))
        result = []
        while h:
            result.append(heapq.heappop(h)[1])
        return result
        