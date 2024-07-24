# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        temp = head.next.next
        start = self.swap(head)
        end = start.next 
        end.next = self.swapPairs(temp)
        return start
    
    def swap(self, node):
        if not node:
            return None
        prev = None
        temp = node.next 
        node.next = prev 
        temp.next = node
        return temp