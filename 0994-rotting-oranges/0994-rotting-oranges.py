class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        goodOrange = 0
        q = deque()
        
        R, C = len(grid), len(grid[0])
        
        for i in xrange(R):
            for j in xrange(C):
                if grid[i][j] == 1:
                    goodOrange += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        time = 0
        while q and goodOrange > 0:
            
            for i in range(len(q)):
                row, col = q.popleft()    
                for dr, dc in direction:
                    r = row + dr
                    c = col + dc

                    if 0 <= r < R and 0 <= c < C and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
                        goodOrange -= 1
            time += 1
            
        return time if goodOrange == 0 else -1