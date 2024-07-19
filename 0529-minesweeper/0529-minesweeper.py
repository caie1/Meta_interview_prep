class Solution(object):
    
    def getAdjMines(self, board, x, y):
        numMines = 0
        for r in xrange(x - 1, x + 2):
            for c in xrange(y - 1, y + 2):
                if 0 <= r < len(board) and 0 <= c < len(board[r]) and board[r][c] == "M":
                    numMines += 1
        return numMines
    
    
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        if not board:
            return board
        
        x, y = click
        
        if board[x][y] == "M": # If we click the mine cell
            board[x][y] = "X"
        else:
            numMines = self.getAdjMines(board, x, y) 
            if numMines: # If we click the empty cell with adj mines
                board[x][y] = str(numMines)
            else: # If we click the empty cell with no adj mines
                board[x][y] = "B"
                
                for r in xrange(x - 1, x + 2):
                    for c in xrange(y - 1, y + 2):
                        if  0 <= r < len(board) and 0 <= c < len(board[r]) and board[r][c] != "B":
                            self.updateBoard(board, [r,c])
        return board