#QUESTION:
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]


#CODE:
def dutchFlag(arr):
    l = 0
    r = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] == 0 and i != l:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
            i -= 1
        elif arr[i] == 2 and i != r:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
            i -= 1
    
    #return arr
            
