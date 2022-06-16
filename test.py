# Input :  Postfix : AB+CD-*
# Output : Prefix :  *+AB-CD
# Explanation : Postfix to Infix : (A+B) * (C-D)
#               Infix to Prefix :  *+AB-CD

# A B +
# +AB C D -
# +AB -CD *
# *+AB-CD

postfix = "AB+CD-*"
postfix = list(postfix)
stack = []

for i in range(0, len(postfix)):
    relOrd = ord(postfix[i]) - ord("A")
    if(relOrd >= 0 and relOrd <= 26):
        stack.append(postfix[i])
    else:
        elem2 = stack.pop()
        elem1 = stack.pop()
        stack.append(postfix[i] + elem1 + elem2)
print(stack[0])

