class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # https://leetcode.com/problems/combination-sum/discuss/742449/Explanation-of-Time-Complexity
        ###N -> elem in candidates 
        ##M is target sum
        ##At each level of recursive tree we have N choices to select
        ##depth of the recursive tree would M
        ##Hence Time O(N*M) Space O(M) ##stack of backtrack
        
        ##Erase this solution
        result = []
        def _recursion(k, comb, curSum):
            if curSum == target:
                result.append(comb)
            elif curSum < target:
                for i in range(k, len(candidates)):
                    _recursion(i, comb + [candidates[i]], curSum + candidates[i])
        _recursion(0, [], 0)
        return result
        
        
        
        
        result = []
        def helper(k, seq, cursum):
            if cursum == target: ## Did we hit the target? 
                result.append(seq)
            elif cursum < target: ## Is cursum still < target
                for i in range(k, len(candidates)): ## Start iterating on candidates - starting position k
                    helper(i, seq + [candidates[i]], cursum + candidates[i]) ## Instead of increamenting i, pass it as it is. As we can use same candidates unlimited amount of time
        helper(0, [], 0)
        return result         
        
        res = []
        
        def backtrack(start, end, seq, sum):
            if sum == 0:
                res.append(seq[:])
            elif sum > 0:
                for i in range(start, end): 
                    seq.append(candidates[i])  ###select    
                    backtrack(i, end, seq, sum - candidates[i])   ###Backtrack
                    seq.pop()  ###deselect
                    
        backtrack(0, len(candidates), [], target)
        
        return res