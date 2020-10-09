#QUESTION:
#Given a singly linked list, determine if it is a palindrome.

#**Notes:**
#[] -> true, [1] -> true, [1,0,1] -> true. So the approach of putting elements in a stack and popping them as the reverse is encountered, will not work.

#Better soln: Finding the length of the list and adding half list to stack (all if even and all-mid if odd). Then we compare both. O(n) time and space.
#CODE:
def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        stack = []
        ptr = head
        length = 0
        while ptr:
            length += 1
            ptr = ptr.next
        
        ptr = head
        while len(stack) < (length // 2):
            stack.append(ptr.val)
            ptr = ptr.next
        
        if length % 2 == 1:
            ptr = ptr.next
        
        while stack:
            if ptr.val != stack.pop():
                return False
            ptr = ptr.next
            
        return True

#Best soln: O(n) time & O(1) space: Finding the middle of the list (traverse entire list once) and reversing list from there. Then we compare both.
#CODE:
(Doing)
