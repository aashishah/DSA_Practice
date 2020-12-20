"""
QUESTION:
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
"""

#CODE:
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        subarray = set()
        maxSum = -999999
        cursum = 0
        while l < len(nums) and l <= r:
            while r < len(nums):
                if nums[r] in subarray:
                    break
                else:
                    subarray.add(nums[r])
                    cursum += nums[r]
                    r += 1
                
            maxSum = max(maxSum, cursum)
            subarray.remove(nums[l])
            cursum -= nums[l]
            l += 1
            
        return maxSum 
        

