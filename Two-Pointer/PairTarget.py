#QUESTION:
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target = 6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2 + 4 = 6


#CODE:
def targetSum(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        total = arr[l] + arr[r]
        if total == target:
            return [l + 1, r + 1]
        elif total < target:
            l += 1
        else:
            r += 1
    return -1  
        
