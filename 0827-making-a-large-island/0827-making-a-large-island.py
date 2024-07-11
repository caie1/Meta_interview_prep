class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
            Run dfs to precompute areas of existing islands first with labeling them
            Run 4 directional bfs on each 0s to figure if we are hitting any of the island, if so 
            then calculate the max area for that 0
        
        """
        self.islandId = -1
        self.islandAreas = {}
        self.directions = [ (1,0),(-1,0),(0,1),(0,-1)]
        
        N = len(grid)
        
        for i in xrange(N):
            for j in xrange(N):
                if grid[i][j] == 1:
                    area = self.dfs(i, j, grid) # We are calculating area of that island with lable self.islandId
                    self.islandAreas[self.islandId] = area # We are storing that precomputed area for label
                    self.islandId -= 1 # Decrement the label to avoid misinterpreting grid data
        maxArea = 0
        # Now, we will find largest island by connecting single zero
        for i in xrange(N):
            for j in xrange(N):
                if not grid[i][j]: # Below code will only work if there's a 0 in the grid
                    area = 1
                    neighbourhood = set()  # We put the labels neighbouring that 0 in set to avoid double counting 
                    for dr, dc in self.directions:
                        row = i + dr
                        col = j + dc
                        
                        if 0 <= row < N and 0 <= col < N and grid[row][col] != 0:
                            neighbourhood.add(grid[row][col]) # grid[row][col] = label of that island
                        
                    for label in neighbourhood:
                        area += self.islandAreas[label]
                    maxArea = max(maxArea, area)
        
        return maxArea if maxArea else N**2 # If no 0 in the grid, return total cells in the grid
    
    def dfs(self, i, j, grid):
        if 0 <= i < len(grid) and 0 <= j < len(grid) and grid[i][j] == 1:
            grid[i][j] = self.islandId

            area = 1

            for dr, dc in self.directions:
                r = i + dr
                c = j + dc

                area += self.dfs(r,c,grid)
            return area
        else:
            return 0
        