"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        newNode = Node(insertVal)
        newNode.next = newNode
        
        if not head:
            return newNode
        
        cur = head
        
        while cur:
            if cur.val <= insertVal <= cur.next.val:
                break
            if cur.val > cur.next.val: # 3 ->[4] 1 2
                if cur.val <= insertVal > cur.next.val: # 3 4 1 2 & insertVal = 5
                    break
                if cur.val > insertVal <= cur.next.val: # 3 4 1 2 & insertVal = 0
                    break
            if cur.next == head: # If we reach end without meeting above, newNode at the end
                break
            cur = cur.next 
        
        newNode.next = cur.next 
        cur.next = newNode
        return head