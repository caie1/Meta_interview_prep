# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.val = float("inf")
    
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        """
        How the Key Function Works:

        For each value x (either root.val or closest), the key function returns a tuple (abs(target - x), x).
        abs(target - x): This calculates the absolute difference between x and the target. It tells us how far x is from the target.
        x: This is included as a tie-breaker to ensure that if two values have the same distance from the target, the smaller value is chosen.
        
        Using the Key Function in min:

        When min compares root.val and closest, it uses the tuples returned by the key function.
        For example, if target = 12, root.val = 15, and closest = 10:
        For root.val (15): lambda x: (abs(12 - 15), 15) returns (3, 15). For closest (10): lambda x: (abs(12 - 10), 10) returns (2, 10). 
        min then compares these tuples: (3, 15) vs. (2, 10). Since 2 (the first element of the tuple) is less than 3, min determines that 10 is closer to 12 than 15.         Thus, closest remains 10.
        """
        
        
        
        
        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x:(abs(target - x), x))
            root = root.left if target < root.val else root.right
        return closest
