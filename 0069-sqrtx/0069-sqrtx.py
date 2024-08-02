class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return x
        l, r = 1, x // 2 + 1
        ans = 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if mid*mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans