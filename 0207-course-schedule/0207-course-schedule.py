class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courseMap = defaultdict(list)
        for crs, pre in prerequisites:
            courseMap[pre].append(crs)
            
        indegree = [0]*numCourses
        
        for pre in courseMap.keys():
            for crs in courseMap[pre]:
                indegree[crs] += 1
        
        q = deque()
        
        for i, v in enumerate(indegree):
            if v == 0:
                q.append(i)
        count = 0
        while q:
            node = q.popleft()
            
            for i in courseMap[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
            count += 1
            
        return count == numCourses
        