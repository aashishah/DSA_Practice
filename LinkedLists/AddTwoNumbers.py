'''
QUESTION:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''


CODE:
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        ans = ListNode(0)
        curr = ans
        
        while ptr1 or ptr2:
            p, q = 0, 0
            if ptr1:
                p = ptr1.val
                ptr1 = ptr1.next
            if ptr2:
                q = ptr2.val
                ptr2 = ptr2.next
                
            total = carry + p + q
            curr.next = ListNode(total % 10)
            carry = total // 10
            curr = curr.next
        
        if carry != 0:
            curr.next = ListNode(carry)
        
        return ans.next
