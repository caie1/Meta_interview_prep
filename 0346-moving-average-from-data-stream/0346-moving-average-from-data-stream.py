class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.q = deque()
        self.average = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        total = 0
        
        if len(self.q) < self.size:
            total = self.average * len(self.q) + val
                
        else:
            total = self.average * len(self.q)
            temp = self.q.popleft()
            total = total - temp + val
            
        self.q.append(val)
        self.average = float(total / len(self.q))
        return self.average
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)