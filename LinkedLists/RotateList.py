#CODE: Partial test cases passed.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
            
        fast = slow = head
        count = 0
        while count < k:
            if not fast:
                fast = head
            fast = fast.next
            count += 1
        
        if not fast:
            return head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            
        head = slow.next
        fast.next = head
        slow.next = None
        
        return head
  
 *******
 
#CODE: Calculating length of list first to find actual K reduces time:

  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        tmp = head
        length = 0
        
        while tmp:
            tmp = tmp.next
            length += 1
            
        k = k % length
        if k == length or k == 0:
            return head

        fast = slow = head
        count = 0
        while k > 0:
            fast = fast.next
            k -= 1
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        fast.next = head
        head = slow.next
        slow.next = None
        
        return head
