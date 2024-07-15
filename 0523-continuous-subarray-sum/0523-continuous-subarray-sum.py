class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        """
        Crux of this algorithm is if we hit same remainder once again that means 
        we have successfully crossed a subsequence with sum divisible by k.
        """
        
        remainder = { 0 : -1} # map remainders with its end index 
        total = 0
        
        for i, n in enumerate(nums):
            total += n
            r = total % k
            
            if r not in remainder:
                remainder[r] = i
            else:
                if i - remainder[r] >= 2:
                    return True
        
        return False