class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        """
         arr = [ 2, 3, 4, 7, 11] now normally for this array it should have been 
         [1,2,3,4,5] so missing values till the index of the array can be found like
         missing values = arr[ind] - (ind + 1). In the end of the while loop r will point to missing < k and l at r + 1
         and loop terminates. now for that r, it is sure that next index will have missing values higher than k
         so to find the answer derrivation goes as follow;
         for above case, loops stops and r points to 7 where it should have been 4 and missing numbers till 7 is 3 and 6 for 11.
         hence to find kth missing number from 7, we can add 2 more missing numbers to 3 where missing numbers are going to be 
         greater than 7 for sure and less than 11 since missing number count at 11 is 6 which is higher than k=5.
         so kth missing number will be 7 + k - missing numbers till 7 = 7 + k - 3 = 7 + 2 =9
         so  we need to return following expression;
         = arr[high] + k - (arr[high] - high + 1)
         = high + 1 + k or
         = low + k
        """
        
        n = len(arr)
        l, r = 0, n - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            missingNums = arr[mid] - (mid + 1)
            
            if missingNums < k:
                l = mid + 1
            else:
                r = mid - 1
        return r + k + 1