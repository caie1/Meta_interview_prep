class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        Find leftmost smallest number and rightmost largest number
        """
        if num <= 11:
            return num 
        numArray = deque([])
        
        # Below loop result: num = 1234 numArray = [1,2,3,4]
        while num:
            numArray.appendleft(num % 10) # appendleft appends from left
            num //= 10
        
        maxSeen = -1
        maxSeenAt = len(numArray)
        
        i = len(numArray) - 1
        
        while i >= 0:
            curNum = numArray[i]
            numArray[i] = [curNum, maxSeen, maxSeenAt]
            if maxSeen < curNum:
                maxSeen = curNum
                maxSeenAt = i
            i -= 1
        i = 0
        
        while i < len(numArray):
            if numArray[i][0] < numArray[i][1]:
                numArray[i][0], numArray[numArray[i][2]][0] = numArray[numArray[i][2]][0], numArray[i][0]
                break
            i += 1
        
        num = 0
        
        for i, _, _ in numArray:
            num = num * 10 + i
        
        return num