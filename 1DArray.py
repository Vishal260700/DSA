"""
Given an array arr[] of n elements in the following format 
{a1, a2, a3, a4, .., an/2, b1, b2, b3, b4, ., bn/2}, 
the task is shuffle the array to {a1, b1, a2, b2, a3, b3, , an/2, bn/2} 
without using extra space.
"""
# O(n), O(1)
def shuffleArray(self, arr, n):
    for i in range(n//2):
        arr.append(arr[i])
        arr.append(arr[i + n//2])
    arr[:] = arr[n:]
    return arr


"""
Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.
Note: Left and right side elements can be equal to required element. And extreme elements cannot be required element.
"""
# Time Complexity - O(n) and Space Complexity - O(n)
def findElement(arr, n):
    
    # left largest is smaller than curr
    # right smallest is lesser than curr
    
    LR = []
    maxSoFar = arr[0]
    for i in range(1, n):
        if(arr[i] >= maxSoFar):
            LR.append(arr[i])
        maxSoFar = max(maxSoFar, arr[i])
    
    RL = set()
    minSoFar = arr[-1]
    for i in range(n-2, -1, -1):
        if(arr[i] <= minSoFar):
            RL.add(arr[i])
        minSoFar = min(minSoFar, arr[i])
    
    for elem in LR:
        if(elem in RL):
            return elem
    return -1

"""
Four Sum Array
"""
def find4Numbers( A, n, X):
    A.sort()
    for i in range(0, len(A) - 3):
        for j in range(i+1, len(A) - 2):
            l = j+1
            r = len(A) - 1
            while(l < r):
                if(A[l] + A[r] + A[i] + A[j] == X):
                    return True
                elif(A[l] + A[r] + A[i] + A[j] < X):
                    l += 1
                else:
                    r -= 1
    return False

"""
Find first non repeated element in array
"""
## Two String traversal, O(n), O(n)
def nonrepeatingCharacter(self,s):
    arr = list(s)
    hashMap = {}

    for i in range(len(arr) - 1, -1, -1):
        if(arr[i] not in hashMap):
            hashMap[arr[i]] = 1
        else:
            hashMap[arr[i]] += 1

    for i in range(0, len(arr)):
        if(hashMap[arr[i]] == 1):
            return arr[i]
    return "$"
# Single traversal, O(n) O(1)
def nonrepeatingCharacter(self,s):
    counter = [[0, 0] for x in range(256)]

    arr = list(s)
    for i in range(0, len(arr)):
        elem = arr[i]
        counter[ord(elem)][0] += 1
        counter[ord(elem)][1] = i
    
    res = 2**31 + 1
    for count in counter:
        if(count[0] == 1):
            res = min(res, count[1])
    return arr[res] if(res != 2**31 + 1) else -1

"""
The cost of stock on each day is given in an array A[] of size N. 
Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
Note: Output format is as follows - (buy_day sell_day) (buy_day sell_day)
For each input, the output should be in a single line.
LOGIC :- increase start mein buy, decrease end mein sell
"""
def stockBuySell(price, n):
    res = []
    i = 0
    BuyBool = False
    transaction = []
    while(i < len(price) - 1):
        
        curr = price[i]
        next = price[i+1]
        
        if(next > curr and not BuyBool):
            transaction.append(i)
            BuyBool = True
        elif(next < curr and BuyBool):
            transaction.append(i)
            res.append(transaction)
            BuyBool = False
            transaction = []
        i += 1
    
    if(BuyBool):
        transaction.append(i)
        res.append(transaction)
        transaction = []
        BuyBool = False
    
    for ans in res:
        print("({buy} {sell})".format(buy = str(ans[0]), sell = str(ans[1])), end = " ")

"""
Given a string str and another string patt. Find the minimum index of the character in str that is also present in patt.
"""
#Function to find the minimum indexed character.
def minIndexChar(self,Str, pat): e
    hashMap = {}
    arr = list(Str)
    for i in range(0, len(arr)):
        if(arr[i] not in hashMap):
            hashMap[arr[i]] = i
    
    res = 2**31 + 1
    for elem in pat:
        if(elem in hashMap):
            res = min(res, hashMap[elem])
    return res if(res != 2**31 + 1) else -1

"""
String is it possible to be rearranged into a palindrome
"""
def isPossible(self, S):
    hashMap = {}
    for char in S:
        if(char not in hashMap):
            hashMap[char] = 0
        hashMap[char] += 1
    
    odds = 0
    for key in hashMap.keys():
        if(hashMap[key]%2 != 0):
            odds += 1
            if(odds > 1):
                return False
    return True

"""
Top K Frequent elements
"""
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hashMap = {}
    for i in range(0, len(nums)):
        if(nums[i] not in hashMap):
            hashMap[nums[i]] = [i, 1]
        else:
            hashMap[nums[i]][1] += 1
    
    res = []
    for key in hashMap.keys():
        res.append([key] + hashMap[key])
    res = sorted(res, key=lambda x: x[2], reverse=True)
    
    ans = []
    for i in range(k):
        ans.append(res[i][0])
    return ans

"""
Exteral file with a number of logs, analyse and put in a directory where we have certain max size allowed if exceeded remove max elem from directory to make space for new elem
"""
import heapq
class LogAnlayser:
    def __init__(self):
        self.logs = []
        self.capacity = 10
        self.maxSize = 10

    def insertLog(self, newLog):
        size = len(newLog)
        if(size > self.maxSize):
            print("Max heap size exceeded")
            return
        data = newLog
        if(self.capacity >= size):
            # insert
            heapq.heappush(self.logs, (-1*size, data))
            self.capacity -= size
        else:
            # remove one log (max size wala) or (min size wala) as per strategy
            elem = heapq.heappop(self.logs)
            freeSize = -1 * elem[0]
            self.capacity += freeSize
            self.insertLog(newLog)
    
    def printLog(self):
        for log in self.logs:
            print("{size}: {info}".format(size=-1*log[0], info=log[1]))

logger = LogAnlayser()
logs = [[123, 234], [123, 234, 234, 234, 234, 234, 234, 234], [123, 234, 234, 234, 234, 234, 234, 231, 234, 234, 234, 234, 234]]
for log in logs:
    logger.insertLog(log)
    print("*********")
    logger.printLog()
            

#Function to find the smallest window in the string s consisting
#of all the characters of string p.
def smallestWindow(self, s, p):
    
    s = list(s)
    p = list(p)
    
    if(len(s) < len(p)):
        return "-1"
    
    data = [0 for x in range(256)]
    
    # count represent all unique charecters in the pattern
    count = 0
    for char in p:
        data[ord(char)] += 1
        if(data[ord(char)] == 1):
            count += 1
    
    # start point
    start = 0
    # ans represent length of smallest window with p in s[start: start + ans]
    ans = len(s) + 1
    
    # Two pointers
    i = 0
    j = 0
    
    while(j < len(s)):
        
        data[ord(s[j])] -= 1
        if(data[ord(s[j])] == 0):
            # this char has reached the limit we want
            count -= 1
            
            # triggered if count reached zero i.e. all are found in i: j
            while(count == 0):
                # now we remove uncessary ones from left side with count == 0
                
                # Global ans
                if(ans > j - i + 1):
                    ans = j - i + 1
                    start = i
                
                # local changes to window
                data[ord(s[i])] += 1
                if(data[ord(s[i])] > 0):
                    count += 1
                i += 1
        
        j += 1
    
    if(ans > len(s)):
        return "-1"
    return ''.join(s[start: start + ans])


"""
Find frequencies of charecters in an strng and spell in sorted order
"""
# Approach 1 - Sort the string and then read through it and get the result
# O(nlogn) and O(1)
string = "aabccccddd"
string = list(string)
string.sort()

currChar = string[0]
count = 1
res = ""
for i in range(1, len(string)):
    if(currChar != string[i]):
        res = res + currChar + str(count)
        currChar = string[i]
        count = 0
    count += 1
if(count != 0):
    res += currChar + str(count)
print(res)

# Approach 2 - Get a hashmap, read through the charecters update the frequence in hashmap
# And then re-read through the hashmap and print in sorted order
# O(n) and O(1)
data = [0 for x in range(256)]
for char in string:
    data[ord(char)] += 1

res = ""
for i in range(0, len(data)):
    if(data[i] != 0):
        res += chr(i) + str(data[i])
print(res)

"""
Count sub arrays with product less than K
"""
def countSubArrayProductLessThanK(self, a, n, k):
        
    left = 0
    right = 0
    prod = 1
    count = 0
    
    while(right < len(a)):
        # update prod with new prod
        prod = prod * a[right]
        
        # reduce window to point where it satisfy k condition
        while(prod > k and left < right):
            prod = prod//a[left]
            left += 1
        
        # adding new elem in all other sub-arrays and itself (1)
        if(prod < k):
            count = count + right - left + 1

"""
Given a string S with repeated characters. The task is to rearrange characters in a string such that no two adjacent characters are the same.
Note: The string has only lowercase English alphabets and it can have multiple solutions. Return any one of them.
"""
## Rearrange charecters 
def rearrangeString(self, str):
        
    if(str == ""):
        return "-1"
    
    # lowercase chars
    data = [0 for x in range(26)]
    
    # calc freq and maxCount, maxChar
    maxCount = 0
    maxChar = 0
    for char in str:
        data[ord(char) - ord("a")] += 1
        if(maxCount < data[ord(char) - ord("a")]):
            maxCount = data[ord(char) - ord("a")]
            maxChar = char
    
    # cant set to even positions and have no repeat
    if(maxCount > (len(str) + 1)//2):
        return "-1"
    
    res = [None for x in range(0, len(str))]
    index = 0
    while(maxCount):
        res[index] = maxChar
        index += 2
        maxCount -= 1
    
    data[ord(maxChar) - ord("a")] = 0
    
    for i in range(26):
        char = chr(i + ord("a"))
        while(data[i] > 0):
            if(index >= len(str)):
                index = 1
            res[index] = char
            data[i] -= 1
            index += 2
    
    return "".join(res)

"""
Postfix to prefix
"""
# Input :  Postfix : AB+CD-*
# Output : Prefix :  *+AB-CD
# Explanation : Postfix to Infix : (A+B) * (C-D)
#               Infix to Prefix :  *+AB-CD

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

"""
Infix to postfix
"""
#Function to convert an infix expression to a postfix expression.
def InfixtoPostfix(self, exp):
    # + * ^ 
    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }
    
    stack = []
    
    exp = list(exp.lower())
    res = []
    for char in exp:
        
        # charecter check
        relOrd = ord(char) - ord("a")
        if(relOrd >= 0 and relOrd <= 26):
            res.append(char)
        else:
            if(char == "("):
                stack.append("(")
            elif(char == ")"):
                while(len(stack) and stack[-1] != "("):
                    res.append(stack.pop())
                stack.pop()
            else:
                # operators
                # if precedence of curr char is smaller than prev one
                # pop out from stack until the last in stack is smaller than curr
                while(len(stack) and stack[-1] != "(" and precedence[char] <= precedence[stack[-1]]):
                    if(char == "^" and stack[-1] == char):
                        break
                    res.append(stack.pop())
                stack.append(char)
    while(len(stack)):
        res.append(stack.pop())
    return "".join(res)