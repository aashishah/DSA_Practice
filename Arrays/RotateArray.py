#Question:
#Given an array, rotate the array to the right by k steps, where k is non-negative.


#CODE:
#O(n) O(n) T&S
class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        
#O(n) O(1) T&S
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            arr[(i + k) % n] = nums[i]
            
        nums[:] = arr
