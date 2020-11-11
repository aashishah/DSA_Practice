Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#CODE:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum
            
            
