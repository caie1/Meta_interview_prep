class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # We cant give label as sum of ASCII values as different combination can give equal sum.
        # One way to solve is using prime number labels and using multiplier instead of sum
        
        res = defaultdict(list)
        
        for s in strs:
            count=[0]*26
            
            for c in s:
                count[(ord(c)-ord('a'))] += 1
            res[tuple(count)].append(s)
        
        return res.values()
        
        
        
        
        