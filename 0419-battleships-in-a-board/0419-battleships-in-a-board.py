class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        n = len(board[0])
        
        count = 0
        visit = set()
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == "X" and (i,j) not in visit:
                    self.dfs(i, j, visit, board)
                    count += 1
        return count
    """
    1) Since the way we are doing the search for X, if the battleship is in horizontal direction, we will always hit the leftmost point of the battleship.
    2) Similarly, for the ship in the vertical direction, we will always hit the topmost point of the battleship
    """
    def dfs(self, r, c, visit, board):
        visit.add((r, c))
        
        # Assume the valid board
        # Check for the horizontal ship alignment
        if c + 1 < len(board[0]) and board[r][c + 1] == "X" and (r,c + 1) not in visit:
            self.dfs(r, c + 1, visit, board)
        
        # Check for the vertical ship alignment
        if r + 1 < len(board) and board[r + 1][c] == "X" and (r + 1, c) not in visit:
            self.dfs(r + 1, c, visit, board)