class Solution(object):

    
    """
    Intuition:
        Given a list of positive values, we are asked to randomly pick up a value based on the weight of each value. To put it simple, the task is to do sampling with weight. Let  us look at a simple example. Given an input list of values [1, 9], when we pick up a number out of it, the chance is that 9 times out of 10 we should pick the number 9 as the answer. In other words, the probability that a number got picked is proportional to the value of the number, with regards to the total sum of all numbers. To understand the problem better, let us imagine that there is a line in the space, we then project each number into the line according to its value, i.e. a large number would occupy a broader range on the line compared to a small number. For example, the range for the number 9 should be exactly nine times as the range for the number 1. Now, let us throw a ball randomly onto the line, then it is safe to say there is a good chance that the ball will fall into the range occupied by the number 9. In fact, if we repeat this experiment for a large number of times, then statistically speaking, 9 out of 10 times the ball will fall into the range for the number 9.
        """
        
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefixSum = []
        
        self.tot = 0
        
        for i, v in enumerate(w):
            self.tot += v
            self.prefixSum.append(self.tot)
        

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.uniform(0, self.tot)
        
        l, r = 0, len(self.prefixSum) - 1
        
        while l < r:
            mid = (l + r) // 2
            if self.prefixSum[mid] <= target:
                l = mid + 1
            else:
                r = mid
        
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()