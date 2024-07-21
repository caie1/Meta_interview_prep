class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l, r = 0, len(arr) - k
        while l < r:
            mid = (l + r) // 2
            upperBound = arr[mid + k]
            if x - arr[mid] <= upperBound - x:
                r = mid
            else:
                l = mid + 1
        return arr[l : r + k]

