class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Greedy
        nums.sort()
        ind = len(nums) // 2
        return nums[ind]