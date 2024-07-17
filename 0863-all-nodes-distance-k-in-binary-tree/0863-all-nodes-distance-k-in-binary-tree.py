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
        
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        """
        1. Build parent dictionary
        2. Use deque and push target node with distance 0
        3. Start performing BFS from target node 
        Time O(N) Space O(N)
        """
        # self.root, self.target = root, target
        # self._K = K
        # self._preorder(root, None)
        # return self._BFS()
        
        parent_map = {}
        def _preorder(node, parent):
            if node:
                parent_map[node] = parent
                _preorder(node.left, node)
                _preorder(node.right, node)
        _preorder(root, None)
        if target not in parent_map:
            return []
        ## BFS
        dq = deque([(target, 0)])
        visited = {target}
        while dq:
            node, dist = dq.popleft()
            if dist == K:
                return [node.val] + [n.val for n, d in dq] 
            for nei in [node.left, node.right, parent_map[node]]:
                if nei and nei not in visited:
                    dq.append((nei, dist + 1))
                    visited.add(nei)
        return []
        
        
        
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
