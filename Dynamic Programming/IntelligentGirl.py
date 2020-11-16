#QUESTION:
Given a string of integers, find the number of even integers present from each index to the very end.
Example:
 Input: 574674546476
 Output: 7 7 7 6 5 5 4 4 3 2 1 1

#CODE:
def findCount(s):
    dp = [0]*len(s)
    if int(s[0]) % 2 == 0:
        dp[-1] = 1
    for i in range(len(s) - 2, -1, -1):
        if int(s[0]) % 2 == 0:
            dp[i] = dp[i + 1]  + 1
        else:
            dp[i] = dp[i + 1]
        
    return dp

s = input()
arr = findCount(s)
for i in arr:
    print(i, end="", sep=" ")
