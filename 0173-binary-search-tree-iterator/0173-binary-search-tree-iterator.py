# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.extract(root)
    
    def extract(self, node):
        while node:
            self.stack.append(node)
            node = node.left        
        
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop() # Next is valid call as per the question requirements
        
        if node.right:
            self.extract(node.right)
        return node.val
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    
#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.res = []
        
#         self.helper(root, self.res)
        
#         self.pointer = - 1
#         self.length = len(self.res)
        
        
#     def helper(self, node, arr):
#         if not node:
#             return None
        
#         self.helper(node.left, arr)
#         arr.append(node.val)
#         self.helper(node.right, arr)
        
#     def next(self):
#         """
#         :rtype: int
#         """
#         self.pointer += 1
#         if self.pointer < self.length:
#             return self.res[self.pointer]

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         if self.pointer == self.length - 1:
#             return False
#         return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()