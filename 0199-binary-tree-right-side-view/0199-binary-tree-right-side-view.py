# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def helper(node, level):
            if not node:
                return None
            if level == len(result):
                result.append(node.val)
            helper(node.right, level + 1)
            helper(node.left, level + 1)
        helper(root, 0)
        return result