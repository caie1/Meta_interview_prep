class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = defaultdict(list)

        for a, b in tickets:
            adj[a].append(b)

        for val in adj.values():
            val.sort(reverse = True)

        result = []

        def dfs(node):
            dest = adj[node]

            while dest:
                nxt = dest.pop()
                dfs(nxt)

            result.append(node)
        dfs("JFK")
        return result[::-1]