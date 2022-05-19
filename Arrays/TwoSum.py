class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hm = {}
        
        for i in range(n):
            val = target - nums[i]
            if val in hm:
                return [hm[val], i]
            hm[nums[i]] = i
