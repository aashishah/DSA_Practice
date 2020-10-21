#QUESTION:
Suppose you have a long flowerbed in which some of the plots are planted and some are not.
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without 
violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True


#CODE:
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:  
        i = 0
        length = len(flowerbed)
        while n and i < length:
            if flowerbed[i] == 0 and ( i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                n = n - 1
                flowerbed[i] = 1
            i += 1
            
        return n == 0
