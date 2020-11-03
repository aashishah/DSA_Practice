#QUESTION:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#CODE:
#Using hash table in linear time.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashT = {}
        for n in nums:
            if n in hashT:
                hashT[n] += 1
            else:
                hashT[n] = 1
        
        for n in hashT:
            if hashT[n] == 1:
                return n
                
#Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
#We can XOR all bits together to find the unique number in linear time and constant space.
#CODE:
class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res ^= n
        return res
