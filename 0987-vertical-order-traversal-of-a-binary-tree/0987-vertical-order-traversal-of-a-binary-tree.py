# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.minCol = 0
        self.maxCol = 0
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        _map = defaultdict(list)
        
        def _helper(node, row, col):
            
            if node:
                _map[col].append((row, node.val))
                self.minCol = min(self.minCol, col)
                self.maxCol = max(self.maxCol, col)
                _helper(node.left, row + 1, col - 1)
                _helper(node.right, row + 1, col + 1)
        _helper(root, 0, 0)
        result = []
        for col in range(self.minCol, self.maxCol + 1):
            collect = []
            for _, val in sorted(_map[col]):
                collect.append(val)
            result.append(collect)
        return result
