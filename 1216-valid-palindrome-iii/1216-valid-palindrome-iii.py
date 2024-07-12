class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
        # Using longest common subsequence solution 
        
        n=len(s)
        t=s[::-1]

        #dp=[[0]*(n+1) for _ in xrange(n+1)]

        prev=[0]*(n+1)

        for i in xrange(1,n+1):
            cur=[0]*(n+1)
            for j in xrange(1,n+1):
                if s[i-1]==t[j-1]:
                    cur[j]=1+prev[j-1]
                else:
                    cur[j]=max(prev[j],cur[j-1])
            prev=cur
        return n - prev[n] <= k                   
        
        
        # DP - memoization from scratch using valid palindrome-ii idea 
        l, r = 0, len(s) - 1
        memo = {}
        def helper(l, r, k):
            if k < 0:
                return False
            if l == r:
                return True
            if (l, r, k) in memo:
                return memo[(l, r, k)]
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    memo[(l, r, k)] = helper(l + 1, r, k - 1) or helper(l, r - 1, k - 1)
                    return memo[(l, r, k)]
            return True
        
        return helper(l, r, k)