class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        visit = set()
        patterns = set()
        
        def bfs(row, col, orgr, orgc):
            
            q = deque()
            q.append((row, col))
            direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            
            while q:
                r, c = q.popleft()
                
                for dr, dc in direction:
                    newr, newc = r + dr, c + dc
                    
                    if 0 <= newr < R and 0 <= newc < C and grid[newr][newc] == 1 and (newr, newc) not in visit:
                        q.append((newr, newc))
                        visit.add((newr, newc))
                        pattern.append(((newr - orgr, newc - orgc)))
            patterns.add(tuple(pattern))
        
        for i in range(R):
            for j in range(C):
                if (i, j) not in visit and grid[i][j] == 1:
                    pattern = []
                    visit.add((i, j))
                    bfs(i, j, i, j)

        return len(patterns)