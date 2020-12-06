#QUESTION:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

#CODE: TC: O(2^(m+n)) SC: O(2^(m+n))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        
        right = self.uniquePaths(m, n-1)
        down = self.uniquePaths(m - 1, n)
        
        return right + down
        
#This is the recursive solution, which  works perfectly, but isn't optimised. Fails at a 23 x 12 matrix grid since there are too many recursive calls in the stack.
#So we optimise the code by memoizing the solution.

#MEMOIZED SOLUTION:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def helperUniquePaths(m, n, memo):
            if (m, n) in memo:
                return memo[(m, n)]
            elif m == 1 and n == 1:
                return 1
            elif m == 0 or n == 0:
                return 0
            memo[(m, n)] = helperUniquePaths(m, n - 1, memo) + helperUniquePaths(m - 1, n,  memo)
            
            return memo[(m,n)]
        
        return helperUniquePaths(m, n, memo)
        
  #TABULATED (iterative) SOLUTION: TC: O(mn) SC: O(mn)
  class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * (n + 1) for j in range(m + 1)]
        memo[1][1] = 1
        print(memo)
        
        for r in range(m + 1):
            for c in range(n + 1):
                if r + 1 <= m:
                    memo[r + 1][c] += memo[r][c]
                if c + 1 <= n:
                    memo[r][c + 1] += memo[r][c]
        
        return memo[m][n]
            
  
  



 
