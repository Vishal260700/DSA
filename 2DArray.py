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

"""
Check if given word can be placed in given crossword puzzle
"""
# O(n*n*m) n - len of board, m - len of word
def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
    # O(n*n*m) n - len of board, m - len of word
    def isValid(board, y, x, word):
        
        # horizontal check
        forWardCount = 0
        backWardCount = 0
        for i in range(0, len(word)):
            if(x + i >= len(board[0])):
                break
            if(board[y][x + i] == word[i] or board[y][x + i] == " "):
                forWardCount += 1
            if(board[y][x + i] == word[len(word) - 1 - i] or board[y][x + i] == " "):
                backWardCount += 1
        
        if(forWardCount == len(word) or backWardCount == len(word)):
            for xi in range(x-1, -1, -1):
                if(board[y][xi] == "#"):
                    break
                else:
                    return False
            
            for xi in range(x + len(word), len(board[0])):
                if(board[y][xi] == "#"):
                    break
                else:
                    return False
            
            return True
        
        # vertical check
        forWardCount = 0
        backWardCount = 0
        for i in range(0, len(word)):
            if(y + i >= len(board)):
                break
            if(board[y + i][x] == word[i] or board[y + i][x] == " "):
                forWardCount += 1
            if(board[y + i][x] == word[len(word) -1 - i] or board[y + i][x] == " "):
                backWardCount += 1
        
        if(forWardCount == len(word) or backWardCount == len(word)):
            for yi in range(y-1, -1, -1):
                if(board[yi][x] == "#"):
                    break
                else:
                    return False
            
            for yi in range(y + len(word), len(board)):
                if(board[yi][x] == "#"):
                    break
                else:
                    return False
            return True
        
        return False
    
    word = list(word)
    for y in range(0, len(board)):
        for x in range(0, len(board[y])):
            if(board[y][x] != "#" and isValid(board, y, x, word)):
                return True
    return False

# O(n^2) - get all horizontal and vertical possible strings and then check for those with len == givenWord and strict check for both forward and backward givenWord
def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
    xWords = []
    yWords = []
    
    for y in range(0, len(board)):
        xWordArr = list(filter(None, ("".join(board[y])).split("#")))
        for elem in xWordArr:
            xWords.append([elem])
    
    for x in range(0, len(board[0])):
        yWord = ""
        for y in range(0, len(board)):
            yWord += board[y][x]
        yWordArr = list(filter(None, yWord.split("#")))
        for elem in yWordArr:
            yWords.append([elem])
    
    checkWords = xWords + yWords
    words = [list(word), list(reversed(list(word)))]
    for Word in checkWords:
        if(len(Word) == 0):
            continue
        Word = list(Word[0])
        if(len(Word) == len(word)):
            for w in words:
                count = 0
                for j in range(0, len(Word)):
                    if(w[j] == Word[j] or Word[j] == " "):
                        count += 1
                if(count == len(word)):
                    return True
    return False

"""
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. 
A four-person group occupies four adjacent seats in one single row. 
Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, 
but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, 
which means to have two people on each side.
"""

# O(N) and O(N*M)
def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    # _ _ _ | * * * * | _ _ _
    
    # _ * * | * * _ _ | _ _ _
    
    # _ _ _ | _ _ * * | * * _
    
    cinema = {}
    for i in range(n):
        cinema[i] = [0 for x in range(0, 10)]
    
    for seat in reservedSeats:
        row = seat[0]
        seatNo = seat[1]
        cinema[row - 1][seatNo - 1] = 1
    
    count = 0
    for key in cinema.keys():
        row = cinema[key]
        
        # independent cases
        commonFlag = False
        if(row[1] == 0 and row[2] == 0 and row[3] == 0 and row[4] == 0):
            commonFlag = True
            count += 1
        
        if(row[5] == 0 and row[6] == 0 and row[7] == 0 and row[8] == 0):
            commonFlag = True
            count += 1
        
        if(row[3] == 0 and row[4] == 0 and row[5] == 0 and row[6] == 0 and commonFlag is False):
            count += 1
    
    return count

def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    # _ _ _ | * * * * | _ _ _
    
    # _ * * | * * _ _ | _ _ _
    
    # _ _ _ | _ _ * * | * * _
    
    cinema = {}
    for i in range(n):
        cinema[i] = [1, 1, 1]
    
    for seat in reservedSeats:
        row = seat[0]
        seatNo = seat[1]
        
        if(seatNo >= 2 and seatNo <= 5):
            cinema[row - 1][0] = 0
        
        if(seatNo >= 6 and seatNo <= 9):
            cinema[row - 1][2] = 0
        
        if(seatNo >= 4 and seatNo <= 7):
            cinema[row - 1][1] = 0
    
    count = 0
    for key in cinema.keys():
        left = cinema[key][0]
        mid = cinema[key][1]
        right = cinema[key][2]
        
        commonFlag = False
        if(left == 1):
            count += 1
            commonFlag = True
        
        if(right == 1):
            count += 1
            commonFlag = True
        
        if(mid == 1 and commonFlag is False):
            count += 1
    return count