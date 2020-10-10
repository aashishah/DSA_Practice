#QUESTION:
#Write a program that outputs the string representation of numbers from 1 to n.
#But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
#For numbers which are multiples of both three and five output “FizzBuzz”.
#Example:
#n = 15,

""" Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
] """


#CODE:
def fizzBuzz(self, n: int) -> List[str]:
        return ["FizzBuzz" if i % 15 == 0 else ("Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)) for i in range(1, n+1)]
