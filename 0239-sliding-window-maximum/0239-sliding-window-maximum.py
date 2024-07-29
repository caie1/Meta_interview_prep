class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        l = r = 0
        q = deque() # Index
        # queue will store elements in decreasing order for the given sliding window
        while r < len(nums):
            # Pop elements of queue if they are smaller than nums[r]
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # Out of bound condition for l pointer
            if q[0] < l:
                q.popleft() 
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res
            