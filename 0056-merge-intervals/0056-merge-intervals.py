class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        result = []
        for i in range(len(intervals)):
            if not result or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result      
        
        
        
        
        
        res = []
        intervals.sort(key = lambda x:x[0])
        i = 0
        
        while i < len(intervals) - 1:
            if intervals[i][1] < intervals[i+1][0]: # If [1,3],[4,6] then no issue
                res.append(intervals[i])
            else: # else we modify the next interval
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            i += 1
        res.append(intervals[i])
        return res