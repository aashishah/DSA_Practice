#QUESTION:
#Detect if a linked list has a cycle.

#Using 2 pointers- fast and slow. In a circle they will eventually meet each other, hence cycle is detected.
#CODE:
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
        
