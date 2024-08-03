class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        #T: O(N + M + max(N,M))
        #S: O(N + M)
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        l = r = 0
        
        while l < len(v1) or r < len(v2):
            i1 = int(v1[l]) if l < len(v1) else 0
            i2 = int(v2[r]) if r < len(v2) else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
            l += 1
            r += 1
        return 0
        