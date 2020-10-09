#QUESTION:
#Reverse the order of words in a given sentence (an array of characters).
         #"Hello World" -----> "World Hello"
         
#Complexity: O(n) Time, O(1) Space

#CODE:
def reverseStr(s):
    words = list(s.split(" ")) #O(n)
    words = words[::-1] #O(n)
    return ' '.join(words) #O(n)

print(reverseStr("Hello World"))
        
#Space is not O(1) however.
