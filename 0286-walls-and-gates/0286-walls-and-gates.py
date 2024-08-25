class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        Row, Col = len(rooms), len(rooms[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        
        for i in range(Row):
            for j in range(Col):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            L = len(q)
            for i in range(L):
                row, col, dist = q.popleft()
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    if (0 <= r < Row) and (0 <= c < Col) and rooms[r][c] not in (-1, 0):
                        if dist + 1 < rooms[r][c]:
                            rooms[r][c] = dist + 1
                            q.append((r, c, dist + 1))
        