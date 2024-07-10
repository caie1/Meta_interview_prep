"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        # This is hare rabbit problem type question
        # Intuition: Remember the Two branched LinkedList merge point detection method without         sets 
        pPrime = p
        qPrime = q
        
        while pPrime != qPrime:
            pPrime = pPrime.parent if pPrime else q
            qPrime = qPrime.parent if qPrime else p
        
        return pPrime