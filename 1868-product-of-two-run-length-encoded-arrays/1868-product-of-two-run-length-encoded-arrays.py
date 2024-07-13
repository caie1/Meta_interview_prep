class Solution(object):
    def findRLEArray(self, e1, e2):
        """
        :type encoded1: List[List[int]]
        :type encoded2: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        
        i = j = 0
        
        while i < len(e1) and j < len(e2):
            if result and (e1[i][0] * e2[j][0]) == result[-1][0]:
                result[-1][1] += min(e1[i][1], e2[j][1])
            else:
                result.append([e1[i][0] * e2[j][0], min(e1[i][1], e2[j][1])])
            if e1[i][1] < e2[j][1]:
                e2[j][1] -= e1[i][1]
                i += 1
            elif e1[i][1] > e2[j][1]:
                e1[i][1] -= e2[j][1]
                j += 1
            else:
                i += 1
                j += 1
        
        return result