class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Optimization can be made with comparing the count of alphabets in board to that of words. If found less means 
        # a straightforward False
        R=len(board)
        C=len(board[0])
        path=set()
        
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0 or c<0 or r>=R or c>=C or word[i]!=board[r][c] or (r,c) in path):
                return False
            path.add((r,c))
            res = ( dfs(r+1,c,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r,c-1,i+1)) 
            path.remove((r,c))
            return res

        for r in range(R):
            for c in range(C):
                if dfs(r,c,0):
                    return True
        return False