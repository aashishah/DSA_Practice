"""
Find peak value in a given array. 
Intuition:
The comparison A[i] < A[i+1] in a mountain array looks like [True, True, True, ..., True, False, False, ..., False]: 1 or more boolean Trues, followed by 1 or more boolean False. For example, in the mountain array [1, 2, 3, 4, 1], the comparisons A[i] < A[i+1] would be True, True, True, False.
"""

#CODE

def peakIndexInMountainArray(self, A: List[int]) -> int:
        low, high = 0, len(A) - 1
        while low < high:
            mid = (low + high) // 2
            if A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid
                
        return low
