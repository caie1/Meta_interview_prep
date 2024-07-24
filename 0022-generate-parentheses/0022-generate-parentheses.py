class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def helper(path, open, close):
            if open == close == n:
                res.append(path)
                return 
            
            if open < n:
                helper(path + "(", open + 1, close)
            if open > close:
                helper(path + ")", open, close + 1)
        
        helper("", 0, 0)
        return res