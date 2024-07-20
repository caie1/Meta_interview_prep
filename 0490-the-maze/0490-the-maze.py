class Solution(object):
    def hasPath(self, maze, start, dest):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        """
        Stopped set will have all the (row, col) where ball can stop including those out of range values as well. If by following any path, we will add new stop values and explore all the directions for that (row, col) otherwise if  we encounter stopped value which is already in the set, we will continue since we have already explored it. This will ensure that if destination is where ball stops will definitely be part of our stack
        """
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        stopped = set()
        stack = [start]
        m, n = len(maze), len(maze[0])
        
        while stack:
            row, col = stack.pop()
            
            if [row, col] == dest:
                return True
            
            for dr, dc in direction:
                nwr = row
                nwc = col
                while 0 <= nwr + dr < m and 0 <= nwc + dc < n and maze[nwr + dr][nwc + dc] == 0:
                    nwr += dr
                    nwc += dc
                if (nwr, nwc) in stopped:
                    continue
                else:
                    stopped.add((nwr, nwc))
                    stack.append([nwr, nwc])
        
        return False