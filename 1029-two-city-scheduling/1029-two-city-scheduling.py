class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key = lambda x : (x[0] - x[1]))
        
        cost = 0
        n = len(costs)
        i = 0
        
        while i < n:
            if i < n / 2:
                cost += costs[i][0]
            else:
                cost += costs[i][1]
            i += 1
        return cost
        