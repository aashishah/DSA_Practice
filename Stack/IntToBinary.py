#Using stack convert an integer to binary.

#CODE:
def intToBinary(num):
    stack = []
    while num >= 1:
        stack.append(str(num % 2))
        num = num // 2
    stack = stack[::-1]

    return int("". join(stack))
