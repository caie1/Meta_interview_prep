class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def solve(x, ind):
            if x == 0:
                return 0
            
            if ind == 0:
                return 1
            
            res = solve(x, ind//2)
            res = res*res 
            return x*res if ind%2 else res
        
        res = solve(x, abs(n))
        return res if n >= 0 else 1/ res
        