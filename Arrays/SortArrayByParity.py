
#QUESTION:
#Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#You may return any answer array that satisfies this condition.

#Notes: Brute force of literally doing what asked will not work since output limit is exceeded. Hence use sorting using two-pointers. This can be used since order does not 
matter and we are simply moving odd elements to the right side.

#CODE:
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 != 0:
                A[i], A[j] = A[j], A[i]
                j -= 1
            else:
                i += 1
                
        return A
