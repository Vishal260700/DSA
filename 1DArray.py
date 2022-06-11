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