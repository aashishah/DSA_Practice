#QUESTION:
#Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

#CODE:
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
            
        return None
