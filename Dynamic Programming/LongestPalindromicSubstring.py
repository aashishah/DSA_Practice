class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        longest = ''
        dp = [[None for i in range(len(s))] for j in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[j][i] = True
                elif j == i+1:
                    dp[j][i] = (s[i] == s[j])
                else:
                    dp[j][i] = (dp[j-1][i+1] and s[i] == s[j])
                if dp[j][i] and j - i + 1 > len(longest):
                    longest = s[i:j+1]
        return longest
        
#Check:
class Solution(object):
    def longestPalindrome(s):
        self.maxLen = 0
        self.maxStr = ''
        def expandAroundCenter(left, right):
            l,r=left,right
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            if r-l-1 > self.maxLen:
                self.maxStr = s[l+1:r]
                self.maxLen = r-l-1
        for i in range(0,len(s)):
            expandAroundCenter(i,i)
            expandAroundCenter(i,i+1)
        return self.maxStr
