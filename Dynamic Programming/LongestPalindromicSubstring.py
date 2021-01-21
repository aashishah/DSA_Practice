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
        
