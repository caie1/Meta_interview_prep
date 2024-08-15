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
        pPrime = p
        qPrime = q
        
        while (pPrime != qPrime):
            pPrime = pPrime.parent if pPrime.parent else q
            qPrime = qPrime.parent if qPrime.parent else p
        
        return pPrime