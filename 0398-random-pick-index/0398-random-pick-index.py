class Solution:

    def __init__(self, nums: List[int]):
        
        self.intMap = defaultdict(list)        
        for i, num in enumerate(nums):
            self.intMap[num].append(i)
            
    def pick(self, target: int) -> int:
        L = len(self.intMap[target])
        
        return self.intMap[target][int(random.uniform(0,L))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)