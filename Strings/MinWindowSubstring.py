"""
QUESTION:
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

[Note: This is a leetcode question and the answer passes all test cases for non-repetative string only.]
"""
#CODE:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minW = 9999999999
        indexes = []
        ans = ""
        if t in s:
            return t
        if len(t) > len(s):
            return ""
        
        for i in range(len(t)):
            try:
                indexes.append(s.index(t[i]))
            except:
                return ans
            
        left, right = min(indexes), max(indexes)
        allPresent = False
        
        while left < right and (right - left) + 1 >= len(t) and right < len(s):
            subset = s[left:right+1]
            for each in t:
                if each in set(subset):
                    allPresent = True
                else:
                    allPresent = False
                    break
                    
            if allPresent and len(subset) < minW:
                minW = len(subset)
                ans = subset
            else:
                right += 1
            left += 1
        return ans
