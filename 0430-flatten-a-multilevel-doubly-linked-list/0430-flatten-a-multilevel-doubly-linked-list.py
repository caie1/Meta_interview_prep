"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        '''
        T(N) S(N)
        '''
        if not head:
            return None
        
        stack = [head]
        dummy = prev = Node(-1, None, None, None)
        
        while stack:
            cur = stack.pop()
            prev.next = cur
            cur.prev = prev
            
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            prev = cur
        
        dummy.next.prev = None # To detach dummy node from head
        
        return dummy.next