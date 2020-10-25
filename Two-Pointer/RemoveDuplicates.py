#QUESTION:
#Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

#Input: nums = [1,1,2]
#Output: 2, nums = [1,2]

#CODE:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        while l < len(nums) and r < len(nums):
            if nums[l] == nums[r]:
                del nums[r]
            else:
                l += 1
                r += 1
        return len(nums)
