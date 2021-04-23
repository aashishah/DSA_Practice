#EXPLANATION:
'''
Lexicographically: In dictionary order
The O(N) inplace algorithm is not easy. It is indeed tricky. The editorial has a nice explanation along with a nice animation.
Use the example: [1,5,8,4,7,6,5,3,1]
Start from the end and scan leftwards till you find the first number which breaks the decreasing sequence. In this case it is 4.
Now if we swap 4 and 7, we will definitely get a larger number than the current one. But that is not the next smallest number.
We want to replace 4 with a digit which is just larger than 4 - smallest number larger than 4 on right. That is 5. We swap the two and get: [1,5,8,5,7,6,4,3,1]
Now [1,5,8,5,7,6,4,3,1] > [1,5,8,4,7,6,5,3,1], but not the smallest number larger than it. If we reverse all digits after 5, we will get the first number in that sequence. [1,5,8,5,1,3,4,6,7]
'''

#CODE:
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length = len(nums)
        i = length - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i < 0:
            nums.sort()
        else:
            j = i + 1
            while j < length and nums[j] > nums[i]:
                j += 1
            j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = nums[:i:-1]
        
