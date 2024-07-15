class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        charMap = defaultdict(int)
        
        for i in xrange(len(order)):
            charMap[order[i]] = i
        
        
        
        for i in xrange(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            
            l = min(len(w1), len(w2))
            if charMap[w1[0]] > charMap[w2[0]]:
                return False
            elif charMap[w1[0]] < charMap[w2[0]]:
                continue
            else:
                j = 0
                l = min(len(w1), len(w2))
                while j < l and w1[j] == w2[j]:
                    j += 1
                    if j < l and charMap[w1[j]] > charMap[w2[j]]:
                        return False
                if j == len(w2) and len(w2) < len(w1):
                    return False
        return True
            
            
            