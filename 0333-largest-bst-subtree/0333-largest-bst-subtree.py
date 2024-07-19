# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.largestBST = 1
        
        self.dfs(root)
        
        return self.largestBST
    
    def dfs(self, node): # Bottom up approach
        if not node:
            return (False, 0, -10001, 10001) # isBST, Size, minVal, maxVal seen until now
        
        if not node.left and not node.right: # Child is itself a BST
            return (True, 1, node.val, node.val)
        
        leftBSTCheck, leftSize, leftMin, leftMax = self.dfs(node.left)
        rightBSTCheck, rightSize, rightMin, rightMax = self.dfs(node.right)
        
        if (leftBSTCheck and rightBSTCheck) and (leftMax < node.val < rightMin):# If both sides are BST
            curSize = 1 + leftSize + rightSize
            self.largestBST = max(self.largestBST, curSize)
            return (True, curSize, leftMin, rightMax)
        elif (leftBSTCheck and not node.right) and (leftMax < node.val): # Only left side is a BST
            curSize = 1 + leftSize
            self.largestBST = max(self.largestBST, curSize)
            return (True, curSize, leftMin, node.val)
        elif (not node.left and rightBSTCheck) and (node.val < rightMin): # Only right side is a BST
            curSize = 1 + rightSize
            self.largestBST = max(self.largestBST, curSize)
            return (True, curSize, node.val, rightMax)
        else: # None is a BST
            return (False, 0, -10001, 10001)
            