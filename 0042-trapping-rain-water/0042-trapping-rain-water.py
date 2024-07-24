class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        leftMax = rightMax = -1
        
        l, r = 0, len(height) - 1
        
        while l < r:
            leftMax = max(leftMax, height[l])
            water += leftMax - height[l]
            rightMax = max(rightMax, height[r])
            water += rightMax - height[r]
            
            if leftMax < rightMax:
                l += 1
            else:
                r -= 1
                
        return water