#QUESTION:
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

#CODE:
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        res = ['0', '1']
        org, flipped = [], []
        for i in range(n - 1):
            for x in res:
                org.append('0' + x)
            for x in res[::-1]:
                flipped.append('1' + x)
            res = org + flipped
            org, flipped = [], []

        return list(map(lambda x: int(x,2), res))
