#QUESTION:
#Given a square matrix mat, return the sum of the matrix diagonals.
#Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

#CODE:
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        j = len(mat) - 1
        ans = 0
        for i in range(len(mat)):
            ans += mat[i][i]
            ans += mat[i][j]
            j -= 1
        
        if len(mat) % 2 != 0:
            ans -= mat[len(mat)//2][len(mat)//2]
        
        return ans
        
