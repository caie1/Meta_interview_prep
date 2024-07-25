class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for i in range(len(words)):
            words[i] = list(words[i])
        for i in (words[0]):
            t = True
            for j in range(1,len(words)):
                if i in words[j]:
                    words[j].remove(i)
                else:
                    t = False
                    break
            if t:
                ans.append(i)
        return ans