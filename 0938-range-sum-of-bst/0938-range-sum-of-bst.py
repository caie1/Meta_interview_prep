# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.total = 0
        
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        # Optimized Solution
        def helper1(node, l, r):
            if not node:
                return 0
            if node.val < l:
                return helper1(node.right, l, r)
            if node.val > r:
                return helper1(node.left, l , r)
            return helper1(node.left, l, node.val) + node.val + helper1(node.right, node.val, r)
        
        return helper1(root, low, high)
        
        # Basic PreOrder Solution
        def helper(node):
            if not node:
                return None
            if low <= node.val <= high:
                self.total = self.total + node.val
            
            helper(node.right)
            helper(node.left)
        
        helper(root)
        return self.total