class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        def helper(ind, path, target):
            #Base Case
            if target == 0:
                res.append(path)
                return
            
            for i in xrange(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                helper(i + 1, path + [candidates[i]], target - candidates[i])
        
        helper(0, [], target)
        return res
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        candidates.sort()
        res = []
        
        def helper(ind, path, target):
            #Base case
            if target == 0:
                res.append(path)
                return None
            
            for j in xrange(ind, len(candidates)):
                if j > ind and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] > target:
                    break
                helper(j + 1, path + [candidates[j]], target - candidates[j])
        helper(0, [], target)
        return res