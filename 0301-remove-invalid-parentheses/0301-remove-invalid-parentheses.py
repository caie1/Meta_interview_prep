class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.maxLen = -1
        self.res = set()
        
        self.helper(0, s, "", 0, 0)
        return list(self.res)
    
    def helper(self, ind, s, path, open, close):
        if ind == len(s):
            if open == close:
                if len(path) > self.maxLen:
                    self.maxLen = len(path)
                    self.res = {path}
                elif len(path) == self.maxLen:
                    self.res.add(path)
            return
        
        ch = s[ind]
        
        if ch == "(":
            # Consider the open bracket
            self.helper(ind + 1, s, path + ch, open + 1, close)
            # Don't consider and skip
            self.helper(ind + 1, s, path, open, close)
        elif ch == ")":
            # Don't consider and skip
            self.helper(ind + 1, s, path, open, close)
            # Consider the close bracket
            if open > close:
                self.helper(ind + 1, s, path + ch, open, close + 1)
        else:
            # Add non-parenthesis character to the path
            self.helper(ind + 1, s, path + ch, open, close)


        
        
        
        # BackTracking Solution
#         open = close = 0
#         for c in s:
#             if c == "(":
#                 open += 1
#             elif c == ")":
#                 if open > 0:
#                     open -= 1
#                 else:
#                     close += 1
#             else:
#                 continue
#         # Max Removal required
#         K = open + close 
        
#         result = set()
        
#         def helper(index, path, open, close, K):
#             if K < 0:
#                 return 
#             if index == len(s):
#                 if open + close == 0 and K == 0:
#                     result.add(path)
#                     return 
#                 return
#             if s[index] != "(" and s[index] != ")":
#                 helper(index + 1, path + s[index], open, close, K)
#             elif s[index] == "(":
#                 #consider the open bracket
#                 helper(index + 1, path + s[index], open + 1, close, K)
#                 # Dont consider and skip to the next
#                 helper(index + 1, path, open, close, K - 1)
#             else: # Character is ")"
#                 # Consider the close bracket
#                 if open > 0:
#                     helper(index + 1, path + s[index], open - 1, close, K)
#                 elif close < open:
#                     helper(index + 1, path + s[index], open, close + 1, K)
#                 # Dont consider and skip to the next
#                 helper(index + 1, path, open, close, K - 1)
        
#         helper(0,"",0,0,K)
#         return list(result)