class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        R, C = len(matrix), len(matrix[0])
        self.prefixSum = [[0]*(C + 1) for _ in xrange(R + 1)]
        
        for i in xrange(R):
            prefix = 0
            for j in xrange(C):
                prefix += matrix[i][j]
                above = self.prefixSum[i][j + 1]
                self.prefixSum[i + 1][j + 1] = prefix + above
                
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        bottomRight = self.prefixSum[r2][c2]
        above = self.prefixSum[r1 - 1][c2]
        left = self.prefixSum[r2][c1 - 1]
        topLeft = self.prefixSum[r1 - 1][c1 - 1]
        
        return bottomRight - above - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)