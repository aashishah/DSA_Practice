#Check if a given string of paranthesis is balanced or not. Balanced: "{()}[]" Not-Balanced: "{{}", ")]"
#CODE:
def balancedParanthesis(s):
    matches = { '{' : '}', '[' : ']', '(' : ')' }
    stack = []
    for c in s:
        if c in '({[' :
            stack.append(c)
        else:
            if stack and c == matches[stack[-1]]:
                stack.pop()
            elif not stack:
                return "Non-Balanced."
    return "Balanced." if not stack else "Non-Balanced."

#ALTERNATE CODE:
def balancedParanthesis(s):
    matches = { '{' : '}', '[' : ']', '(' : ')' }
    stack = []
    is_balanced = True
    i = 0
    while i < len(s) and is_balanced:
        if s[i] in '({[' :
            stack.append(s[i])
        else:
            if not stack:
                is_balanced = False
            else:
                top = stack.pop()
                if s[i] != matches[top]:
                    is_balanced = False
        i += 1
        
    if not stack and is_balanced:
        return "Balanced."
    else:
        return "Non-Balanced."

