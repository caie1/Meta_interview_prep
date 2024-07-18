class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs(i, j):
            dq = deque([(i, j)])
            while dq:
                i, j = dq.popleft()
                for x, y in directions:
                    newx, newy = i + x, j + y
                    if 0 <= newx < rows and 0 <= newy < cols and grid[newx][newy] == '1' and (newx, newy) not in visit:
                        visit.add((newx, newy))
                        dq.append((newx, newy))

        
        def dfs(r,c, visit, directions):
            visit.add((r,c))
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1" and (row, col) not in visit:
                    dfs(row, col, visit, directions)
            
        rows, cols = len(grid), len(grid[0])    
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        visit = set()
        count = 0
        for i in xrange(rows):
            for j in xrange(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i,j)
                    count += 1
        
        return count