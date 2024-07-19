class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        '''
        Once we found the top-left battelship, we found a battleship. 'X' those are not located top-left of the contagious 'X'
        will not add up to the number of battleship. 
        1. Battleships are not contaigous to each other. 
        2. Battleship are of shape 1*n or n *1        
        '''
        rows, cols = len(board), len(board[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '.':
                    continue
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                count += 1
        return count
        
        
        
        
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