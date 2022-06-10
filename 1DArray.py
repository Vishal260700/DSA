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