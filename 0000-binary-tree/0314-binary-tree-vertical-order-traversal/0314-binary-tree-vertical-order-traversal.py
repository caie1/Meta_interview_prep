# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        min_col, max_col = 0, 0
        _map = defaultdict(list) # col -> list of nodes
        
        dq = deque([(root, 0)])
        
        while dq:
            node, col = dq.popleft()
            _map[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            if node.left:
                dq.append((node.left, col - 1))
            if node.right:
                dq.append((node.right, col + 1))
        result = []
        for col in range(min_col, max_col + 1):
            result.append(_map[col])
        return result
        
        
#         if not root:
#             return []
#         nodeMap = defaultdict(lambda:defaultdict(list))

#         q = deque()
#         q.append([root, 0, 0])

#         while q:
#             node, x, y = q.popleft()
#             if node:
#                 nodeMap[x][y].append(node.val)

#             if node.left:
#                 q.append([node.left, x - 1, y + 1])
#             if node.right:
#                 q.append([node.right, x + 1, y + 1])
#         res = []

#         for i in sorted(nodeMap.keys()):
#             level = []
#             for j in sorted(nodeMap[i]):
#                 level.extend(nodeMap[i][j])
#             res.append(level)
        
#         return res