class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        pairs = 0
        unpair_char_set = set()
        for ch in s:
            if ch in unpair_char_set:
                pairs += 1
                unpair_char_set.remove(ch)
            else:
                unpair_char_set.add(ch)
        return pairs * 2 + 1 if unpair_char_set else pairs * 2

