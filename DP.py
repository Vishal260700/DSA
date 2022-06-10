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