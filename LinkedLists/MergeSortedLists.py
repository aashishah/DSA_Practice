#QUESTION:
#Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

#APPROACH:
#Naive: Merge the linked Lists and sort them. 
#Optimised: Traverse through lists and add elements to new list according to value, since both lists are in increasing order. Time & Space complexity: O(n + m)

#CODE:
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        
        merged = cur = ListNode() 
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            elif l2.val <= l2.val:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        cur.next = l1 or l2
        return merged.next
