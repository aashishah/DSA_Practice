#QUESTION:
#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#There is only one duplicate number in nums, return this duplicate number.

#Naive solution, sort so that duplicates are adjacent. T + S: O(nlogn) + O(1) or O(n)
#CODE:
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
                
#Better Solution: Create a set and return number that repeats. T + S: O(n) + O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for n in nums:
            if n in visited:
                return n
            visited.add(n)
            
#Best: T + S: O(n) + O(1) Cycle Detection
class Solution:
    def findDuplicate(self, nums):
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
