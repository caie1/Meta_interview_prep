class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if len(word) == 0 or len(abbr) == 0:
            return False
        
        i = j = 0
        
        while i < len(word) and j < len(abbr):
            if word[i] != abbr[j]:
                if not abbr[j].isdigit():
                    return False
                else:
                    if abbr[j] == "0": # Leading zero edge case
                        return False
                    else:
                        num = 0
                        while j < len(abbr) and abbr[j].isdigit():
                            num = num * 10 + int(abbr[j])
                            j += 1
                        i += num 
            else:
                i += 1
                j += 1
                
        return i == len(word) and j == len(abbr)