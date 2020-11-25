#CODE:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        freq = {}
        length = len(s)
        while r < length:
            if s[r] not in freq:
                freq[s[r]] = 1
                r += 1
                max_len = max(max_len, r-l)
            else:
                del freq[s[l]]
                l += 1
        
        return max_len
