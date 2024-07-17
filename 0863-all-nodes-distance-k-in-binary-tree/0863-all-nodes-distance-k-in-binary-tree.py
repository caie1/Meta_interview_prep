# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def adjecency(self, root, parentMap):
        q= deque()
        q.append(root)
        
        while q:
            node =q.popleft()
            
            if node.left:
                parentMap[node.left] = node
                q.append(node.left)
            if node.right:
                parentMap[node.right] = node
                q.append(node.right)        
        
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parentMap = {}
        self.adjecency(root,parentMap)
        
    
        q = deque()
        q.append([target,0])
        visited = set([target])
        res = []
        
        while q:
            node, dist = q.popleft()
            
            if dist == k:
                res.append(node.val)
            
            for neighbor in [node.left, node.right, parentMap.get(node)]:
                if neighbor and neighbor not in visited:
                    q.append([neighbor, dist + 1])
                    visited.add(neighbor)
        
        return res  
