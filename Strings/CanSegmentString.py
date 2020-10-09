#QUESTION:
#You are given a dictionary of words and a large input string. 
#You have to find out whether the input string can be completely segmented into the words of a given dictionary. The following two examples elaborate on the problem further.
#Given a dictionary of words.
              #apple | apple | pear | pie
              #Input string of “applepie” can be segmented into dictionary words.
              # apple | pie
              
              
#CODE:
def segmentStrings(s, dictionary):
    for i in range(len(s)):
        first = s[0:i]
        if first in dictionary:
            second = [i:len(s)]
            if not second or second in dictionary or segmentString(second, dictionary):
                return True
     return False
     
#Time: O(2^n) Space: O(n^2)
            
      
