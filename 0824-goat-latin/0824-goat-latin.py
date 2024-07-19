class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split(" ")
        vowels = set(["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"])
        
        for i in xrange(len(sentence)):
            
            if sentence[i][0] in vowels:
                sentence[i] += "ma" + "a"*(i + 1)
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + "ma" + "a"*(i + 1)
        return " ".join(sentence)