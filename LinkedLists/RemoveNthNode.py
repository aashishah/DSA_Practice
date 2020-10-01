"""
QUESTION:
Given a linked list, remove the n-th node from the end of list and return its head.
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

#CODE:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head #store head temporarily 
        l = 0
        ptr = head
        while ptr:
            l += 1
            ptr = ptr.next
        
        ptr = dummy
        while l > n:
            l -= 1
            ptr = ptr.next
            
        ptr.next = ptr.next.next
        return dummy.next
            
        
        
            
                
        
