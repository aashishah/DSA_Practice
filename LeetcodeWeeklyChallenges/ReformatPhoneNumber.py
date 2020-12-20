"""
You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.

You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:

2 digits: A single block of length 2.
3 digits: A single block of length 3.
4 digits: Two blocks of length 2 each.
The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2.

Return the phone number after formatting.
"""
#CODE:
class Solution:
    def reformatNumber(self, number: str) -> str:
        nums = []
        for i in range(len(number)):
            if number[i].isdigit():
                nums.append(number[i])
        
        ans = []
        
        
        rem = len(nums) % 3
        quo = len(nums) // 3
        if rem == 1:
            rem = 4
            quo -= 1
            
        counter = 0
        for _ in range(quo):
            ans.append("".join(nums[counter: counter + 3]))
            counter += 3
        
        final = ""
        if rem == 4:
            final = nums[-4] + nums[-3] + "-" + nums[-2] + nums[-1]
        elif rem == 2:
            final = nums[-2] + nums[-1]
        elif rem == 1:
            final = nums[-1]
        ans.append(final)
        
        if not rem:
            return "-".join(ans)[:-1]
        
        return "-".join(ans)
