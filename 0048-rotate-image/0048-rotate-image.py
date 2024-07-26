class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in xrange(n):
            for j in xrange(i + 1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
        
        l, r = 0, n - 1
        
        while l < r:
            for i in xrange(n):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1
        
        