"""
Traverse matrix in Spiral Order
"""
def solve(matrix, r, c):
    visited = [[False for x in range(c)] for y in range(r)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    index = 0

    total = r*c
    i = 0

    res = []
    currX = 0
    currY = 0
    while(i < total):
        res.append(matrix[currY][currX])
        visited[currY][currX] = True
        newX = currX + dx[index]
        newY = currY + dy[index]
        if(newX < 0 or newX >= c or newY < 0 or newY >= r or visited[newY][newX]):
            index += 1
            index = index%4
            currX += dx[index]
            currY += dy[index]
        else:
            currX = newX
            currY = newY
        i += 1
    return res