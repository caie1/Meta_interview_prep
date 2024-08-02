class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res

    
        if not intervals:
            return [newInterval]
        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] <= newInterval[0]:
                l = mid + 1
            else:
                r = mid - 1
        intervals.insert(l, newInterval)
        result = []
        for i in range(len(intervals)):
            if not result or intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result