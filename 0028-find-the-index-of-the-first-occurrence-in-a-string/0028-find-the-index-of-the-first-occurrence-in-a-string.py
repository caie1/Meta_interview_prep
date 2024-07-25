class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle or (len(haystack) < len(needle)):
            return -1
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i : i + n] == needle:
                return i
        return -1
