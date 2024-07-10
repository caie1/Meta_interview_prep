class Solution(object):
    def helper(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            return int(a/b)
    def calculate(self, s):
        """
        For description see the Basic Calculator III
        Time O(N) Space O(N)
        Questions to ask an interviewer:
        1. Do we have to consider priority based calculation?
        2. Will there be any space in 's'?
        3. Can I consider s be valid expression?
        4. Will there be only single digits in handle? 
        5. What kind of operator we are looking for? 
        
        pop operation on opStack=> when current operator has priority less than or equal to last operator in opStack
        otherwise just push the current operator to the opStack
        When we are traversing an experssion from left to right, suppose we are encountring operator in increasing               priority the we might need to append an extra character to the given expression in order to calculate answer for         the given expression. 
        """
        s = s.replace(' ', '') # if s has space innit
        s += '+'
        priority = {'+' : 0, '-': 0, '*': 1, '/': 1}
        numStack, opStack = [], []
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                k = 0
                while i < len(s) and s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                numStack.append(k)
            else:
                while opStack and priority[ch] <= priority[opStack[-1]]: # If previous sign has igher priority than cur
                    val2 = numStack.pop() # Assume valid string
                    val1 = numStack.pop() # Assume valid string
                    numStack.append(self.helper(val1, val2, opStack.pop()))
                opStack.append(ch)
                i += 1
        return numStack[-1]
