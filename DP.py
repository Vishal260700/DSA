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

"""
Gold mine problem - collect max gold in a grid
"""
def maxGold(self, n, m, M):   
    # O(3*(n*m) - Recursive
    def solve(grid, currX, currY):
        # base case
        if(currX == m - 1):
            return 0
        # DFS
        dy = [0, 1, -1]
        dx = [1, 1, 1]
        
        res = 0
        for i in range(3):    
            newX = currX + dx[i]
            newY = currY + dy[i]
            if(newX >= 0 and newX < m and newY >= 0 and newY < m):
                res = max(res, solve(M, newX, newY) + M[newY][newX])
        return res
    
    res = 0
    for y in range(0, n):
        res = max(res, solve(M, 0, y) + M[y][0])
    return res

    # O(n*m) - Memoized version
    def solve(grid, currX, currY):
        # base case
        if(currX == m - 1):
            return 0
        # DFS
        dy = [0, 1, -1]
        dx = [1, 1, 1]
        
        # Memoized case
        if(DP[currY][currX]):
            return DP[currY][currX]
        
        res = 0
        for i in range(3):    
            newX = currX + dx[i]
            newY = currY + dy[i]
            if(newX >= 0 and newX < m and newY >= 0 and newY < m):
                res = max(res, solve(M, newX, newY) + M[newY][newX])
        DP[currY][currX] = res
        return res
    
    DP = [[None for x in range(0, m)] for y in range(0, n)]
    res = 0
    for y in range(0, n):
        res = max(res, solve(M, 0, y) + M[y][0])
    return res


"""
Letter combinations of phone number
"""
def letterCombinations(self, digits: str) -> List[str]:
    phone = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    
    def solve(digits, ptr):
        
        if(digits[ptr] in phone):
            # base case
            if(ptr == len(digits) - 1):
                return phone[digits[ptr]]
            opts = phone[digits[ptr]]
            # hypothesis - we get all combinations for digits[ptr + 1: ]
            subRes = solve(digits, ptr + 1)
            ans = []
            for opt in opts:
                for res in subRes:
                    ans.append(opt + res)
            return ans
        else:
            raise Exception("Incorrect phone number digit format for messaging")
    
    if(digits == ""):
        return []
    
    digits = list(digits)
    return solve(digits, 0)

## Longest string chain
def longestStrChain(self, words: List[str]) -> int:
    # key - word, value - chain starting from this word
    DP = {}
    res = 0
    words = list(sorted(words, key=len))
    for word in words:
        DP[word] = 1
        for i in range(0, len(word)):
            newWord = word[:i] + word[i+1:]
            if(newWord in DP):
                DP[word] = max(DP[word], DP[newWord] + 1)
            res = max(res, DP[word])
    return res