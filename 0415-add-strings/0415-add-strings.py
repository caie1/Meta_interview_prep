class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ##Time O(max(len(m,n))) Space O(1)
        result = []
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            val1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            val2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            res = val1 + val2 + carry
            result.append(str(res % 10))
            carry = res // 10
            if i >= 0:
                i -= 1
            if j >= 0:
                j -= 1
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])
        
        
        
        
        
        
        