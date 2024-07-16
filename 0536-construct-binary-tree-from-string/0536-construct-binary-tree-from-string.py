# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        '''
        Left node is always there. 
        '''
        if not s:
            return None
        root = TreeNode()
        stack = [root]
        
        i = 0
        
        while i < len(s):
            node = stack.pop()
            num = 0
            if s[i] == "-" or s[i].isdigit():
                isNeg = False
                num = 0
                if s[i] == "-":
                    isNeg = True
                    i += 1

                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num = (- num if isNeg else num)
                node.val = num
                if i < len(s) and s[i] == "(":
                    stack.append(node)
                    node.left = TreeNode()
                    stack.append(node.left)
            elif node.left and s[i] == "(":
                stack.append(node)
                node.right = TreeNode()
                stack.append(node.right)
            i += 1
        return root
            
        
        