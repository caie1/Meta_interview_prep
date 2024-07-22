import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ##Erase this solution:
        majorityElem = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == majorityElem:
                count += 1
            else:
                count -= 1
            if count == 0:
                majorityElem = nums[i]
                count = 1
        return majorityElem

            
        ##Approach 1 Time : O(n) Space : O(n)
        
#         mid = len(nums)/2
#         dictN = defaultdict(int)
#         for num in nums:
#             dictN[num] += 1
        
#         for key, val in dictN.items():
#             if val > mid:
#                 return key

        ##Approach 2 Time : O(nlogn) Space : O(1)
        # nums.sort() ## O(nlogn)
        # return nums[len(nums)//2]
        
        ##Approach 3:
        ##Use count and majority element set to 1 and nums[0] initialially
        ##Increament count if encounter element same as majority element 
        ##Else decrement the count
        ##When you see count as zero them set it to 1 and assign nums[i] as majority element
        
        ##Time O(n) Space O(1)
        count = 1
        majorityElem = nums[0]
        
        for num in nums[1:]:
            if num == majorityElem:
                count += 1
            elif count == 0:
                count = 1
                majorityElem = num
            else:
                count -= 1
        return majorityElem
    
        