class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        result = []
        
        def helper(ind, path):
            if ind == len(s):
                result.append(" ".join(path))
                
            for i in xrange(ind, len(s)):
                if s[ind : i + 1] in wordDict:
                    helper(i + 1, path + [s[ind : i + 1]])
        
        helper(0, [])
        return result