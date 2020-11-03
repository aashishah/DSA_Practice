#QUESTION:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

#CODE:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        actual = 0
        for i, n in enumerate(nums):
            total += n
            actual += i + 1
        return actual - total
        
#More readable version, using Gauss' Formula:

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        actual = n * (n + 1) // 2 #Gauss' Formula
        return actual - total

        
#Using Bit manipulation for even faster results:

#CODE:
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
