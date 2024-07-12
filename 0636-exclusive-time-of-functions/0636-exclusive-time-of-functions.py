class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # More straightforward solution
        result = [0]*n
        stack = []
        for log in logs:
            splitLog = log.split(':')
            funcID = int(splitLog[0])
            status = splitLog[1]
            time = int(splitLog[2])
            if status == 'start':
                stack.append((funcID, time))
            else:
                executionTime = time - stack.pop()[1] + 1
                result[funcID] += executionTime
                if stack:
                    result[stack[-1][0]] -= executionTime
        return result
        
        
        # Simpler Solution
        stack = []
        res = [0]*n
        
        process = logs[0].split(":")
        stack.append([int(process[0]), int(process[2])])
        i = 1
        
        while i < len(logs): # Since every function has start and end we dont need to worry about i == len(logs)
            process = logs[i].split(":")
            process[0] = int(process[0])
            process[2] = int(process[2])
            
            if process[1] == "start":
                if stack:
                    index = stack[-1][0]
                    duration  = process[2] - stack[-1][1]
                    res[index] += duration
                stack.append([process[0], process[2]])
            else: # Assume valid logs hence for end condition, stack will minimum have single process
                index = stack[-1][0]
                duration = process[2] - stack[-1][1] + 1
                res[index] += duration
                stack.pop()
                if stack:
                    stack[-1][1] = 1 + process[2]
            i += 1
        return res
                