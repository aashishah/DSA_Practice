#QUESTION:
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

#CODE:
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ptr1 = 0
        length = len(nums)
        
        while ptr1 < length and nums[ptr1] != 1:
            ptr1 += 1
        if ptr1 == length:
            return True
        
        ptr2 = ptr1 + 1
        
        while ptr1 < length and ptr2 < length: 
            if nums[ptr1] == 1 and nums[ptr2] == 1:
                if (ptr2 - ptr1) - 1 < k:
                    return False
                else:
                    ptr1 = ptr2
                    ptr2 += 1
            elif nums[ptr1] == 1 and nums[ptr2] != 1:
                ptr2 += 1
            else:
                ptr1 += 1
                ptr2 += 1
                
        return True
