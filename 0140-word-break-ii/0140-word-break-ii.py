class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        res = []
        
        def helper(ind, path):
            # Base Case
            if ind == len(s):
                res.append(" ".join(path))
                return None
            
            for i in xrange(ind, len(s)):
                if s[ind : i + 1] in wordDict:
                    helper(i + 1, path + [s[ind : i + 1]])
        helper(0, [])
        return res