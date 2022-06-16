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

"""
Next greater element
"""
# Brute force - O(n^2)
if(len(arr) == 0):
    return []

res = []
for i in range(0, len(arr) - 1):
    Flag = False
    for j in range(i + 1, len(arr)):
        if(arr[j] > arr[i]):
            Flag = True
            res.append(arr[j])
            break
    if(not Flag):
        res.append(-1)
# last elem always have no elem for it in next side
res.append(-1)
return res

# Optimized solution - O(n)
def nextLargerElement(self,arr,n):
    if(len(arr) == 0):
        return []
    
    res = []
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        # pop until we get an elem bigger than curr element
        while(len(stack) > 0 and stack[-1] <= arr[i]):
            stack.pop()
        # add that elem or -1
        res.append(-1 if len(stack) == 0 else stack[-1])
        # add our curr elem in stack for further elements check
        stack.append(arr[i])
    
    return list(reversed(res))

"""
Trapping rainwater
"""
def trappingWater(self, arr,n):
    left = [0 for x in range(n)]
    left[0] = arr[0]
    for i in range(1, n):
        if(len(left) == 0):
            left[i] = arr[i]
        else:
            left[i] = max(arr[i], left[i-1])
    
    right = [0 for x in range(n)]
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])
    
    res = 0
    for i in range(0, n):
        res += (min(left[i], right[i]) - arr[i])
    return res