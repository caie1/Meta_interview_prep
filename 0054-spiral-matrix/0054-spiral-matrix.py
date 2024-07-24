class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        R, C = len(matrix), len(matrix[0])
        l, r, t, b = 0, C - 1, 0, R - 1
        res = []
        
        while l <= r and t <= b:
            
            for i in xrange(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            
            for i in xrange(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            
            if l > r or t > b:
                break
            
            for i in xrange(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            
            for i in xrange(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
        return res