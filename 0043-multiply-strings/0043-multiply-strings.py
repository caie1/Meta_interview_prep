class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        '''num1[i] * num2[j] will be placed at indices [i + j, i + j + 1]'''
        result = [0]*(len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                result[i + j + 1] += int(num1[i]) * int(num2[j])
                result[i + j] += result[i + j + 1] // 10
                result[i + j + 1] %= 10
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1
        result = ''.join([str(x) for x in result[i:]])
        return result if result else '0'

