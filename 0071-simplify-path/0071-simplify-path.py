class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        d = path.split('/')
        stack = []
        
        for val in d:
            if val == "" or val == ".":
                continue
            elif val == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(val)
        
        return "/" + "/".join(stack)