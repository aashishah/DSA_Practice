'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''


#CODE:
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keypad = {"1": "", "2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        
        def dfs(pos, word):
            if pos == len(digits):
                res.append("".join(word))
                return
            
            for ch in keypad[digits[pos]]:
                word.append(ch)
                dfs(pos + 1, word)
                word.pop()
                
        
        dfs(0, [])
        
        return res
