class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not firstList or not secondList:
            return []
        
        res= []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            
            a = max(firstList[i][0], secondList[j][0])
            b = min(firstList[i][1], secondList[j][1])
            if a <= b:
                res.append([a,b])
            
            if firstList[i][1] >= secondList[j][1]: # If first interval ends after second
                j += 1
            else:
                i += 1
        
        return res