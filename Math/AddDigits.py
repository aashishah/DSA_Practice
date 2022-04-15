'''
QUESTION:
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

'''

#CODE:
def addDigits(self, num: int) -> int:
        rem = 0
        while num > 0:
            rem += num % 10
            num //= 10
            
            if num == 0 and rem > 9:
                num = rem
                rem = 0
                
        return rem