class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(r,c, visit, directions):
            visit.add((r,c))
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1" and (row, col) not in visit:
                    dfs(row, col, visit, directions)
            
            
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        visit = set()
        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i,j,visit,directions)
                    count += 1
        
        return count