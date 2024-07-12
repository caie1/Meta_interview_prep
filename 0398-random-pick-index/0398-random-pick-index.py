class Solution:

    def __init__(self, nums: List[int]):
        self.numToIdx = defaultdict(list)
        for i, num in enumerate(nums):
            self.numToIdx[num].append(i)




        # self.num_idx = defaultdict(list)
        # for i, num in enumerate(nums):
        #     self.num_idx[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.numToIdx[target])



        # return random.choice(self.num_idx[target])
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)