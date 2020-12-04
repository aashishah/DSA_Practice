#CODE:
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        count = 0
        i = 0
        def helper(string, i, count):
            num = ""
            if count == 4 and i == len(s):
                res.append(string)
            else:
                while i < len(string):
                    num += string[i]
                    if 0 <= int(num) <= 255 and count < 4:
                        count += 1
                        helper(string[:i+1] + '.' + string[i + 1:len(string)], i, count)
                    i += 1
            return res
                
        return helper(s, i, count)
