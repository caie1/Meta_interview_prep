# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        dummy = ListNode(0)
        temp = dummy
        
        heap = []
        # O(klogk) time complexity 
        for i in xrange(len(lists)):
            if lists[i]:
                val = [lists[i].val, lists[i]]
                heapq.heappush(heap, val)
        # While loop will run for N*K times plus since heap will have at max k elements at any given time
        # So time complexity is O(N*K*logk)
        while heap:
            val, node = heapq.heappop(heap)
            temp.next = node
            
            if node.next:
                ele = [node.next.val, node.next]
                heapq.heappush(heap, ele)
            
            temp = temp.next
        
        return dummy.next
        