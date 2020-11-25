#QUESTION:
#Implement atoi which converts a string to an integer. (Lot's of edge cases on this one)

#CODE:
class Solution:
    def myAtoi(self, s: str) -> int:
        res, i = 0, 0
        s = s.strip()
        if not s:
            return 0
  
        sign = 1
        if s[0] in "+-":
            i += 1
            if s[0] == "-":
                sign = -1
        
        for i in range(i, len(s)):
            if not s[i].isdigit():
                break
            res = res * 10 + int(s[i])
                
        res = res * sign

        if res > 2**31-1:
            return 2**31-1
        if res < -2**31:
            return -2**31
        
        return res
