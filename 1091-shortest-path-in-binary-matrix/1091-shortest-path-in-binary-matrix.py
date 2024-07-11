class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if grid[0][0] == 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        dq = deque([(0, 0, 1)])
        visited = {(0, 0)}
        while dq:
            i, j, dist = dq.popleft()
            if i == rows - 1 and j == cols - 1:
                return dist
            for x, y in directions:
                newx, newy = i + x, j + y
                if 0 <= newx < rows and 0 <= newy < cols and grid[newx][newy] == 0 and (newx, newy) not in visited:
                    visited.add((newx, newy))
                    dq.append((newx, newy, dist + 1))
        return -1
