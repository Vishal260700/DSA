"""
reach nth stair from 0 either 1 or 2 steps
"""
# Recursive solution - O(2^n)
def solve(curr, target):
    if(curr == target):
        return 1
    
    if(curr + 2 > target):
        return solve(curr + 1, target)
    
    return solve(curr + 1, target) + solve(curr + 2, target)
print(solve(0, n))
# Dynamic programming Solution - O(n) and O(n)
def countWays(self,n):
    modulus = 10**9+7
    DP = [None for x in range(n)]
    
    # Recursive solution
    def solve(curr, target):
        # woohoo
        if(curr == target):
            return 1
        
        # Memoized case
        if(DP[curr] is not None):
            return DP[curr]
        
        # Memoization
        if(curr + 2 > target):
            DP[curr] = solve(curr + 1, target)%modulus
            return DP[curr]
        DP[curr] = (solve(curr + 1, target)%modulus + solve(curr + 2, target)%modulus)%modulus
        return DP[curr]
    
    return solve(0, n)

"""
Function to find the maximum money the thief can get.
"""
# Recursive - O(2**n)
def FindMaxSum(self,a, n):
    def solve(curr, arr):
        # base case
        if(curr >= len(arr)):
            return 0
        # Two choices - loot or not
        return max(solve(curr + 2, arr) + arr[curr], solve(curr + 1, arr))
    return solve(0, a)
# Dynamic - O(n)
def FindMaxSum(self,a, n):
    DP = [None for x in range(n)]
    def solve(curr, arr):
        # base case
        if(curr >= len(arr)):
            return 0
        # memoized case - Induction
        if(DP[curr] is None):
            DP[curr] = max(solve(curr + 2, arr) + arr[curr], solve(curr + 1, arr))
        return DP[curr]
    return solve(0, a)

"""
Function to get max path sum in a matrix
"""
# Dynamic Programming - Memoized O(n^2)
def maximumPath(self, N, Matrix):
    # reach bottom y with max sum
    dx = [0, -1, 1]
    dy = [1, 1, 1]
    DP = [[None for x in range(0,len(Matrix[y]))] for y in range(0, len(Matrix))]
    def solve(matrix, currX, currY, targetY):
        # reached end
        if(currY == targetY):
            return matrix[currY][currX]
        # Memoized read
        if(DP[currY][currX]):
            return DP[currY][currX]
        res = 0
        for i in range(3):
            newX = currX + dx[i]
            newY = currY + dy[i]
            if(newX >= 0 and newX < len(matrix[0]) and newY >= 0 and newY < len(matrix)):
                res = max(res, matrix[currY][currX] + solve(matrix, newX, newY, targetY))
        DP[currY][currX] = res
        return res
    res = 0
    for x in range(0, len(Matrix[0])):
        res = max(res, solve(Matrix, x, 0, len(Matrix) - 1))
    return res