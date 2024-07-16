class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        def friendRequest(a, b):
            if b > a: return False
            if b <= ((0.5 * a) + 7): return False
            return True
        
        
        ageGroup = collections.Counter(ages)
        totalRequests = 0
        
        for a, numA in ageGroup.items():
            for b, numB in ageGroup.items():
                if friendRequest(a, b):
                    totalRequests += numA * numB
                    if a == b: totalRequests -= numA  # For same age, double counting
        
        return totalRequests