class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        charMap = {char: i for i, char in enumerate(order)}
        
        def is_sorted(w1, w2):
            for c1, c2 in zip(w1, w2):
                if charMap[c1] != charMap[c2]:
                    return charMap[c1] < charMap[c2]
            return len(w1) <= len(w2) # This will only execute if all the characters matches
        
        for i in range(len(words) - 1):
            if not is_sorted(words[i], words[i + 1]):
                return False
        
        return True
