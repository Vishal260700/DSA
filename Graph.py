"""
Function to find out minimum steps Knight needs to reach target position.
"""
def minStepToReachTarget(self, KnightPos, TargetPos, N):
    # visited
    visited = [[False for x in range(N)] for y in range(N)]
    # coordinates
    currY = KnightPos[0] - 1
    currX = N - KnightPos[1]
    targetY = TargetPos[0] - 1
    targetX = N - TargetPos[1]
    # visited curr node
    visited[currY][currX] = True
    # horse moves
    dx = [2, 2, 1, -1, -2, -2, 1, -1]
    dy = [1, -1, 2, 2, 1, -1, -2, -2]
    # BFS
    queue = []
    queue.append([currY, currX, 0])
    while(queue):
        elem = queue.pop(0)
        Y = elem[0]
        X = elem[1]
        dist = elem[2]
        
        if(Y == targetY and X == targetX):
            return dist
        
        for i in range(8):
            newY = Y + dy[i]
            newX = X + dx[i]
            
            if(newY >= 0 and newY < N and newX >= 0 and newX < N and not visited[newY][newX]):
                visited[newY][newX] = True
                queue.append([newY, newX, dist + 1])
    return -1

"""
Function to find if the given edge is a bridge in graph.
LOGIC:- reach from c to d without direct bridge -> if not possible - return 1 else return 0
"""
def isBridge(self, V, adj, c, d):
    visited = [False for x in range(V)]
    
    def isValid(frm, to):
        if((frm == c and to == d) or (frm == d and to == c)):
            return False
        return True
    
    def dfs(curr, target, graph):
        visited[curr] = True
        if(curr == target):
            return True
        
        res = False
        for n in graph[curr]:
            if(isValid(curr, n) and not visited[n]):
                res = res or dfs(n, target, graph)
        return res
    
    return 0 if(dfs(c, d, adj)) else 1