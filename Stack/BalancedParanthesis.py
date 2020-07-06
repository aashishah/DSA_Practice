#Check if a given string of paranthesis is balanced or not. Balanced: "{()}[]" Not-Balanced: "{{}", ")]"
#CODE:
def balancedParanthesis(s):
    matches = { '{' : '}', '[' : ']', '(' : ')' }
    stack = []
    is_balanced = True
    for c in s:
        if c in '({[' :
            stack.append(c)
        else:
            if stack and c == matches[stack[-1]]:
                stack.pop()
            elif not stack:
                return "Non-Balanced."
    return "Balanced." if not stack else "Non-Balanced."
