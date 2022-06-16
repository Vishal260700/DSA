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


"""
Number of islands in the graph
"""
def numIslands(self,grid):
    # O(row x col)
    def dfs(grid, currX, currY):
        
        visited[currY][currX] = True
        
        dx = [1, -1, 0, 0, 1, -1, 1, -1]
        dy = [0, 0, 1, -1, 1, -1, -1, 1]
        
        for i in range(8):
            
            newX = currX + dx[i]
            newY = currY + dy[i]
            
            if(newX >= 0 and newX < len(grid[0]) and newY >= 0 and newY < len(grid) and visited[newY][newX] is False and grid[newY][newX] == 1):
                dfs(grid, newX, newY)
    
    visited = [[False for x in range(0, len(grid[y]))] for y in range(0, len(grid))]
    islands = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if(grid[y][x] == 1 and visited[y][x] is False):
                dfs(grid, x, y)
                islands += 1
    return islands

"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
"""
def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
    # make a graph
    graph = {}
    for i in range(0, len(equations)):
        frm = equations[i][0]
        too = equations[i][1]
        
        if(frm not in graph):
            graph[frm] = {}
        
        if(too not in graph):
            graph[too] = {}
        
        graph[frm][too] = values[i]
        graph[too][frm] = 1/values[i]
        
    def pathSearch(curr, target, visited):
        visited[curr] = True
        # base case
        if(curr == target):
            return 1
        
        if(curr in graph):
            # check all paths if there is any path i.e. non zero value then 
            for key in graph[curr].keys():
                if(visited[key] is False):
                    tempRes = graph[curr][key] * pathSearch(key, target, visited)
                    if(tempRes != 0):
                        return tempRes
            return 0
        else:
            # we cant reach from here to target
            return 0
    
    res = []
    for query in queries:
        frm = query[0] 
        to = query[1]
        visited = {}
        for key in graph.keys():
            visited[key] = False
        if(frm in graph):
            tempRes = pathSearch(frm, to, visited)
            res.append(tempRes if tempRes != 0 else -1.00000)
        else:
            res.append(-1.00000)
    return res

"""
Given a matrix of dimension R*C where each cell in the matrix can have values 0, 1, or 2 which has the following meaning:
0: Empty ward
1: Cells have uninfected patients
2: Cells have infected patients

An infected patient at ward [i,j] can infect other uninfected patient at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
Help Aterp determine the minimum units of time after which there won't remain any uninfected patient i.e all patients would be infected. 
If all patients are not infected after infinite units of time then simply return -1.
"""
def helpaterp(self, hospital):
    # code here
    
    queue = []
    for y in range(0, len(hospital)):
        for x in range(0, len(hospital[y])):
            if(hospital[y][x] == 2):
                queue.append([y, x, 0])
    
    res = 0
    while(queue):
        curr = queue.pop(0)
        
        X = curr[1]
        Y = curr[0]
        res = max(res, curr[2])
        
        hospital[Y][X] = 2
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            newX = X + dx[i]
            newY = Y + dy[i]
            if(newX >= 0 and newX < len(hospital[0]) and newY >= 0 and newY < len(hospital) and hospital[newY][newX] == 1):
                queue.append([newY, newX, curr[2] + 1])
    
    for y in range(0, len(hospital)):
        for x in range(0, len(hospital[y])):
            if(hospital[y][x] == 1):
                return -1
    return res

"""
You are given an array of employees employees where:

    employees[i].id is the ID of the ith employee.
    employees[i].importance is the importance value of the ith employee.
    employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.

Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.
"""
def getImportance(self, employees: List['Employee'], id: int) -> int:
        
    organisation = {}
    for emp in employees:
        organisation[emp.id] = emp
    
    def dfs(currNode, graph):
        # no more subordinates
        if(len(graph[currNode].subordinates) == 0):
            return 0
        
        # we have subordinates
        res = 0
        for subord in graph[currNode].subordinates:
            res = res + graph[subord].importance + dfs(subord, graph)
        return res
    
    return dfs(id, organisation) + organisation[id].importance

"""
Snake and ladders min number of dice rolls to reach end - O(N) and O(1)
"""
class QueueEntry:
    def __init__(self, val, dist):
        self.val = val
        self.dist = dist

arr = [3, 22, 5, 8, 11, 26, 20, 29, 17, 4, 19, 7, 27, 1, 21, 9]
N = 8

# key -> start, value -> end
ladders = {}
for i in range(0, N, 2):
    ladders[arr[i]] = arr[i+1]
    
snakes = {}
for j in range(N, 2*N, 2):
    snakes[arr[j]] = arr[j+1]

target = 30

visited = [False for x in range(target)]

queue = []
queue.append(QueueEntry(0, 0))
qe = QueueEntry(0, 0)

while(queue):
    qe = queue.pop(0)
    visited[qe.val] = True
    
    if(qe.val == target - 1):
        break
    
    for dice in range(1, 7):
        newQe = QueueEntry(qe.val + dice, qe.dist + 1)
        if(newQe.val < target and visited[newQe.val] is False):

            if(newQe.val in ladders):
                newQe.val = ladders[newQe.val]
            elif(newQe.val in snakes):
                newQe.val = snakes[newQe.val]

            queue.append(newQe)

print(qe.dist)