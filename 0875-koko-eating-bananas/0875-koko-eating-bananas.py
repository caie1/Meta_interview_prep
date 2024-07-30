import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def timeTaken(k, H):
            hours = 0
            
            for pile in piles:
                hours += pile // k
                if pile % k != 0:
                    hours += 1

            return hours <= H

        
        l, r = 1, max(piles)
        
        while l <= r:
            mid = (l + r) // 2
            
            if timeTaken(mid, h):
                r = mid - 1
            elif not timeTaken(mid, h):
                l = mid + 1
        return l