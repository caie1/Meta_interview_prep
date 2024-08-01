# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(preorder, inorder, preStart , preEnd, inStart, inEnd, inorderMap):
            if preStart > preEnd or inStart > inEnd:
                return None
            node = TreeNode(preorder[preStart])
            index =  inorderMap[preorder[preStart]]
            # How many roots are to the left of this node can be calculated from inorder list
            leftroots = index - inStart
            # For any inStart, next few roots are going to be (L-N-R) where Node will be the direct right child
            node.left = build(preorder, inorder, preStart + 1, preStart + leftroots, inStart, index - 1, inorderMap)
            node.right = build(preorder, inorder, preStart + leftroots + 1, preEnd, index + 1, inEnd, inorderMap)
            return node
        
        
        
        inorderMap = {element:index for index, element in enumerate(inorder)}
        root = build(preorder, inorder, 0 , len(preorder) - 1, 0, len(inorder) - 1, inorderMap)
        return root