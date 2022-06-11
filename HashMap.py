"""
Function to count subarrays with sum equal to 0.
"""
def findSubArrays(self,arr,n):
    hashMap = {}
    res = [] # store start, end index
    total = 0
    for i in range(n):
        total += arr[i]
        
        if(total == 0):
            res.append([0, i])
        
        value = []
        if(total in hashMap):
            value = hashMap[total]
            for index in value:
                res.append([index, i])
        value.append(i)
        hashMap[total] = value
    
    # print(res)
    return len(res)

"""
Given an array A of N integers. The task is to find if there are two pairs (a, b) and (c, d) such that a+b = c+d.
"""
def findPairs(self, arr, n):
    hashMap = {}
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            tempTotal = arr[i] + arr[j]
            if(tempTotal not in hashMap):
                hashMap[tempTotal] = []
            hashMap[tempTotal].append([i, j])
            if(len(hashMap[tempTotal]) >= 2):
                return 1
    return 0