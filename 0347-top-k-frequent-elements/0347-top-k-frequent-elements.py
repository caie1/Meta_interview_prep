class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
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
        