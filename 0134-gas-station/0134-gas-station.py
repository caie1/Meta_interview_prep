class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # If sum of gas is less than cost of move then we can never reach given position 
        if (sum(gas)<sum(cost)):
            return -1

        total =0
        res = 0
        # If difference is negative then we cannot start from that position and if its positive we can start from that position
        # When we start from that position, if we can reach the end of the array being positive that means we can easily absorb
        # all the previous costs hence no need to loop back to reach start position because start happens when cumelative sum 
        # hits positive
        
        """
         How this works is lets say, we will only enter the loop situation if first of all sum(gas) > sum(cost). SO when that's
         true, then there exist an index where gas[i] > cost[i] which becomes our start point from where onwards sum of gas will be higher
         than sum of costs such that it can outweight all the negative sums that we encountered reaching that index. That's why we run till 
         the end of the array to see if we can manage positive total
        """
        for i in xrange(len(gas)):
            total += gas[i] - cost[i]
    
            if total <0:
                total = 0 
                res = i + 1

        return res