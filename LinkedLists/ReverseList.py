# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            #store backup
            temp = curr.next
            #reverse the links
            curr.next = prev
            prev = curr
            #move to next node
            curr = temp
        
        return prev
