class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        
        """
        Have a hashmap for count of string t ready, then in string s, go on decrementing for every character you see, if count of                     character goes 0, that means we have fulfilled one required character. when count of fulfilled character equals length of t, then             shring the window with l while incrementing all the values of l and if seen count goes above 0 that means we have shrunk the window           too much
        """
        
        start = -1 
        minLen = float(1e8)
        count = 0
        l = r = 0
        
        char = defaultdict(int)
        
        for i in t:
            char[i] += 1
            
        while r < len(s):
            if char[s[r]] > 0:
                count += 1
            char[s[r]] -= 1
            
            while count == len(t):
                if (r - l + 1) < minLen:
                    minLen = r - l + 1 
                    start = l
                char[s[l]] += 1
                if char[s[l]] > 0:
                    count -= 1
                l += 1
            r += 1
        
        return "" if start == -1 else s[start: start + minLen]