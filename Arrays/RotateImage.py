#QUESTION:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

#Naive approach (but works)- O(N^2)
#CODE:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return [[]]
        #TRANSPOSE OF MATRIX
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        #REVERSE EACH ROW
        for i in range(len(matrix)):
            matrix[i].reverse()
 
 
