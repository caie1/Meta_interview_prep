# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        As soon as we hit Null value in our queue, we should expect all the following values 
        to be Null for Tree to be a complete B-Tree. If rightmost node is absent then it will
        be Null followed by Nulls due to child nodes of the previous layer.
        """
        q = deque([root])
        
        while q:
            node = q.popleft()
            
            if node:
                q.append(node.left)
                q.append(node.right)
            else:
                while q:
                    if q.popleft():
                        return False
        return True