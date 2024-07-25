# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def travelKNodes(self, node, k):
        
        while node and k > 0:
            node = node.next
            k -= 1
        return [node, k]
    
    def reverse(self, node, k): # Reverse k nodes which return head of the reversed list
        prev = None  
        cur = node
        while k > 0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp 
            k -= 1
        return [prev, node] # [start, end]
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """    
        if not head or k == 1:
            return head
        
        p1 = p2 = head
        temp = dummy = ListNode(0)
        
        while p1:
            p2, count = self.travelKNodes(p1, k)
            if not p2 and count > 0:
                temp.next = p1
                break
            temp.next, temp = self.reverse(p1, k)
            p1 = p2
        return dummy.next