"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def __init__(self):
        
        self.first = None
        self.last = None
    
    def inorderLink(self, node):
        if node:
            self.inorderLink(node.left)
            if not self.last:
                self.first = node
            else:
                node.left = self.last
                self.last.right = node

            self.last = node

            self.inorderLink(node.right)
    
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        self.inorderLink(root)
        self.first.left = self.last
        self.last.right = self.first
        
        return self.first