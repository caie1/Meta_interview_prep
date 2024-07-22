# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Questions to ask an interviewer
        1. How are the digits stored?
        2. What number of digits are kept in each node?
        
        T(max(N, M)) S(1) 
        '''
        ## M, N len of l1 and l2 respectively
        ## Time: O(max(M, N)) Space: O(1)
        dummy = prev = ListNode()
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            res = val1 + val2 + carry
            carry = res // 10
            prev.next = ListNode(res % 10)
            prev = prev.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            prev.next = ListNode(carry)
        return dummy.next
            
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        carry = 0
        llist = dummy = ListNode(-1)
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            res = x + y + carry
            dummy.next = ListNode(res % 10)
            carry = res // 10
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            dummy.next = ListNode(carry)
        return llist.next
    
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        carry = 0
        t1 = l1
        t2 = l2
        llist = dummy = ListNode(0)
        
        while t1 or t2:
            x = t1.val if t1 else 0
            y = t2.val if t2 else 0
            total = x + y + carry
            carry = total // 10
            dummy.next = ListNode(total % 10)
            dummy = dummy.next
            
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        if carry > 0:
            dummy.next = ListNode(carry)
        return llist.next
                
            
        # temp = l1
        # str1 = ""
        # while temp:
        #     str1 += str(temp.val)
        #     temp = temp.next
        # str1 = str1[::-1]
        # temp = l2
        # str2 = ""
        # while temp:
        #     str2 += str(temp.val)
        #     temp = temp.next
        # str2 = str2[::-1]
        # res = (str(int(str1) + int(str2)))[::-1]
        # llist = dummy = ListNode(0)
        # for i in res:
        #     dummy.next = ListNode(int(i))
        #     dummy = dummy.next
        # return llist.next
        