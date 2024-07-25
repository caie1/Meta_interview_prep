class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def find(day):
            curTotal = 0
            count = 0
            
            for i in xrange(len(bloomDay)):
                if bloomDay[i] <= day:
                    curTotal += 1
                else:
                    count += curTotal // k
                    curTotal = 0
            count += curTotal // k
            return count >= m
        
        
        if len(bloomDay) < m*k:
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        ans = -1
        
        while l <= r:
            mid = (l + r) // 2
            
            if find(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1    
        return ans
            