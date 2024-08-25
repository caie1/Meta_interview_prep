class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        count = 0
        
        def dfs(node):
            visited.add(node)
            
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
                    
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count