class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        logic = {}
        
        for word in words:
            for ch in word:
                if ch not in logic:
                    logic[ch] = set()
        
        for i in range(1, len(words)):
            
            
            for j in range(min(len(words[i]), len(words[i - 1]))):
                if (words[i][j] != words[i - 1][j]):
                    logic[words[i - 1][j]].add(words[i][j])
                    break
            else:
                if len(words[i - 1]) > len(words[i]):
                    return ""
        
        stack = []
        visited = {}
        
        def dfs(node):
            if node in visited:
                if visited[node] == -1:
                    return True
                else:
                    return False
            
            visited[node] = -1
            
            for nei in logic[node]:
                if dfs(nei):
                    return True
                
            stack.append(node)
            visited[node] = 1
            return False
        
        for char in logic:
            if dfs(char):
                return ""
                
        return ''.join(stack[::-1])