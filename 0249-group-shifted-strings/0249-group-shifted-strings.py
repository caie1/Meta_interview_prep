class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        charMap = defaultdict(list)
        
        
        for string in strings:
            if len(string) == 1:
                charMap[(-1,)].append(string)
            else:
                charDiff = []
                
                for i in xrange(1,len(string)):
                    diff = ord(string[i]) - ord(string[i - 1])
                    charDiff.append( diff % 26)
                charMap[tuple(charDiff)].append(string)
        
        res = []
        
        for v in charMap.values():
            res.append(v)
        
        return res
        