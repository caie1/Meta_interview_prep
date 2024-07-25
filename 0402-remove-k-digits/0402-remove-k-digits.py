class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        
        for i in num:
            while stack and stack[-1] > i and k > 0:
                stack.pop()
                k -= 1
            stack.append(i)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        result = "".join(stack).lstrip("0") # Remove leading zeros if any
        
        return result if result else "0"