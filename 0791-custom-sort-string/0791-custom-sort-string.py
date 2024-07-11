class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        freq = defaultdict(int)
        
        for i in s:
            freq[i] += 1
        
        result = []
        
        for ch in order:
            if ch in freq:
                result.append(ch * freq[ch])
                del freq[ch]
        
        for ch, v in freq.items():
            result.append(ch * v)
        
        return "".join(result)
        