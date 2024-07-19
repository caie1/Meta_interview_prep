# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.foundP = False
        self.foundQ = False
        
        def helper(node):
            if not node:
                return None
            
            left = helper(node.left)
            right = helper(node.right)
            
            if node == p:
                self.foundP = True
                return node
            
            if node == q:
                self.foundQ = True
                return node
            
            if left and right:
                return node
            
            return left if left else right
        
        lca = helper(root)
        return lca if self.foundP and self.foundQ else None
