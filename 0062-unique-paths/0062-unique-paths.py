class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prev=[1]*n

        for i in range(1,m):
            temp=[0]*n
            for j in range(n):
                up=left=0
                up=prev[j]
                if j>0:
                    left=temp[j-1]
                temp[j]=up+left
            prev=temp
            
        return prev[n-1]
