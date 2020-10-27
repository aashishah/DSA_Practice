#QUESTION:
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


#CODE:
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start, sm = 0, 0
        avg = []
        for ptr in range(len(nums)):
            sm += nums[ptr]
            if ptr >= k - 1:
                avg.append(sm / k)
                sm -= nums[start] #slide out the first num
                start += 1
        
        return max(avg)
