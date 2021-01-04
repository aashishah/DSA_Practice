"""
iven an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Example 1:

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

"""
#CODE:
def ceilingNumber(arr, key):    
    length = len(arr)
    lo, hi = 0, length - 1
    smallest = hi
    found = False
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == key:
                return mid

        
        elif arr[mid] < key:
            lo = mid + 1
                
        else:
            hi = mid - 1
            
        if arr[hi] >= key and arr[hi] <= arr[smallest]:
            smallest = hi
            found = True

        if found:
                return smallest
        else:
                return - 1

