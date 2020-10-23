#QUESTION
Problem Statement 
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

#CODE:
def squareSorted(arr):
    l, r = 0, len(arr) - 1
    squared = [0]*len(arr)
    for i in range(len(arr) - 1, 0, -1):
        if abs(arr[l]) > abs(arr[r]):
            squared[i] = arr[l] * arr[l]
            l += 1
        else:
            squared[i] = arr[r] * arr[r]
            r -= 1
    return squared
        
