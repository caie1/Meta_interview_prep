class Solution:

    def __init__(self, nums):
        self.numToIdx = defaultdict(list)
        for i, num in enumerate(nums):
            self.numToIdx[num].append(i)

    def pick(self, target):
        return random.choice(self.numToIdx[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)