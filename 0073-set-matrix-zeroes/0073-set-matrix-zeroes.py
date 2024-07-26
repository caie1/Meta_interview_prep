class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        
        row = set()
        col = set()
        
        for i in xrange(R):
            for j in xrange(C):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        if not row or not col:
            return 
        
        for i in row:
            for j in xrange(C):
                matrix[i][j]=0
        
        for j in col:
            for i in xrange(R):
                matrix[i][j] = 0
                
        