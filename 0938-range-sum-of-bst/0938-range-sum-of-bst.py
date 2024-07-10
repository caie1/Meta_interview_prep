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
        def helper(node):
            if not node:
                return None
            if low <= node.val <= high:
                self.total = self.total + node.val
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return self.total