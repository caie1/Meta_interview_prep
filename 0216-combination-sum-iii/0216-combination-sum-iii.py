class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        
        def helper(i, path, target):
            #Base Case
            if len(path) == k and target == 0:
                res.append(path)
                return
            
            for j in xrange(i, 10):
                if j > target:
                    break
                helper(j + 1, path + [j], target - j)
                
                
        helper(1, [], n)
        return res