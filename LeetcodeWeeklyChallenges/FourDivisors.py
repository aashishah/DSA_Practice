#QUESTION:
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.
If there is no such integer in the array, return 0.

#CODE:
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            divisors = set()
            for i in range(1, floor(sqrt(n)) + 1):
                if n % i == 0:
                    divisors.add(n // i)
                    divisors.add(i)
                
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                ans += sum(divisors)
                
        return ans
        
        """
        NOTE:
        Need to check up to floor(sqrt(num)) = s (inclusive) only because 
        for any divisor d < s, there is another divisor num/d > s.
        E.g. 81 has divisors 1, 3, 9, 27, 81. sqrt(81) = 9 has divisors
        1, 3, 9. 81/1 = 81, 81/3 = 27, 81/9 = 9. So if we only check for 
        divisors up to 9 and account for 81/divisor, we reduce time 
        complexity by sqrt(num).
        """
