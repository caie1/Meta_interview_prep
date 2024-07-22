class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Brute Force Solution
        count = 1
        
        for num in xrange(1, n + 1):
            if n % num == 0:
                if count == k:
                    return num
                count += 1
        return - 1