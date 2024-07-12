"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        nodeMap = {None:None} # old node -> new
        cur = head
        
        while cur:
            nodeMap[cur] = Node(cur.val)
            cur = cur.next 
        
        cur = head
        while cur:
            copy = nodeMap[cur]
            copy.next = nodeMap[cur.next]
            copy.random = nodeMap[cur.random]
            cur = cur.next
        
        return nodeMap[head]
        
        