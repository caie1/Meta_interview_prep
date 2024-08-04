class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = ""
        
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                curStr = ""
                while stack[-1] != "[":
                    char = stack.pop()
                    curStr = char + curStr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*curStr)
        return "".join(stack)
                    