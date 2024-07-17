class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        T(NlogN + N^2) S(1)
        """
        ##Erase this solution
        ## Sort : O(NlogN)
        ## O(N^2)
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    total = nums[i] + nums[j] + nums[k]
                    if total < 0:
                        j += 1
                    elif total > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
        return result
