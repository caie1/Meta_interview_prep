class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        #Tabulation
        dp = [[False]*(n+1) for _ in xrange(m+1)]
        dp[0][0] = True # Empty String matchs empty pattern
        
        
        # Initialize pattern for "*"
        for j in xrange(2,n+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # Zero occurrence
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]
        
        
        # Memoization         
        memo = {}
        
        def match(i,j):

             # Check if the result is already in the memoization cache
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: if the pattern is exhausted, check if the string is also exhausted
            if j == len(p):
                return i == len(s)
            
            # Check if the first characters match (considering '.' as a wildcard)
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # If the next character in the pattern is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two possibilities: skip 'x*' or use '*' to match one more character
                result = match(i, j + 2) or (first_match and match(i + 1, j))
            else:
                # If no '*' is present, just check the first match and move both pointers
                result = first_match and match(i + 1, j + 1)
            
            # Store the result in the memoization cache
            memo[(i, j)] = result
            return result
        
        # Start the recursive matching from the beginning of the string and pattern
        return match(0, 0)