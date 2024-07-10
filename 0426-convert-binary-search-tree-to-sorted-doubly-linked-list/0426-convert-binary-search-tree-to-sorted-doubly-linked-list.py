"""
    Inorder traversal for sorted traversal through tree. If we are travelling from root to 
    left to find the leftmost smallest element, then self.last will be None, which makes us 
    figure out self.first as that smallest elemennt. Then before going for right traversal, 
    update the self.last as last visited element so we can fix the right side
"""

class Solution(object): # T: O(N) if tree is balanced then S: O(logN) if skewed tree S: O(N)
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