class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sumSquare(num):
            sum = 0
            
            while num:
                sum += ((num % 10) ** 2)
                num = int(num // 10)
            return sum
        
        if n == 1:
            return True
        slow = fast = n
        
        while (True):
            slow = sumSquare(slow)
            fast = sumSquare(sumSquare(fast))
            if slow == fast:
                break
        return (slow == 1)
        