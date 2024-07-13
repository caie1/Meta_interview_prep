class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(mat)
        n = len(mat[0])
        total = m * n
        up =True
        i = j = 0
        
        while len(res) < total:
            res.append(mat[i][j])
            
            if up:
                if i == 0 and j < n - 1:
                    j += 1
                    up = not up
                elif j == n - 1:
                    i += 1
                    up = not up
                else:
                    i -= 1
                    j += 1
            else:
                if j == 0 and i < m - 1:
                    i += 1
                    up = not up
                elif i == m - 1:
                    j += 1
                    up = not up
                else:
                    i += 1
                    j -= 1
        
        return res