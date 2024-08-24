class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node, parent):
    
            visited.add(node)
            
            for nei in adj[node]:
                if nei not in visited:
                    if not dfs(nei, node):
                        return False # has cycle
                elif nei != parent:
                    return  False
            
            return True
        
        
        return dfs(0, -1) and len(visited) == n