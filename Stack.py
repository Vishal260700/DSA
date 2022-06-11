"""
Function to check if brackets are balanced or not.
"""
def ispar(self,x):
    opens = set(["[", "{", "("])
    stack = []
    
    for char in x:
        if(char in opens):
            stack.append(char)
        else:
            if(len(stack) == 0):
                return False
            if(stack[-1] == "[" and char == "]") or (stack[-1] == "(" and char == ")") or (stack[-1] == "{" and char == "}"):
                stack.pop()
            else:
                return False
    if(len(stack)):
        return False
    return True