class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = []
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
                res.append("")
            elif c == ")":
                if stack:
                    res[stack.pop()] = "("
                    res.append(c)
                else:
                    res.append("")
            else:
                res.append(c)
        
        return "".join(res)