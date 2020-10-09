#QUESTION:
#Find the middle of the Linked List.

#Method 1:
#Just traverse the entire list, to find length. Then return node at length / 2


#Method 2:
#Have 2 pointers. One traverses 2 nodes at once, while the other traverses one. By the time the faster one reaches the end, the slower one will reach the middle.
#CODE:

def findMid(head):
  fast = slow = head #head points to list.
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
  return slow.val



