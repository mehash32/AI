board = [
    [0,0,0,4,0,0,0,5,0],
    [0,0,0,0,0,8,1,0,2],
    [0,0,0,0,1,9,0,6,0],
    [0,8,5,0,0,0,0,1,0],
    [2,0,6,0,3,0,7,0,8],
    [0,7,0,0,0,0,6,2,0],
    [0,3,0,6,4,0,0,0,0],
    [4,0,8,5,0,0,0,0,0],
    [0,6,0,0,0,2,0,0,0]
]
def printBoard(bo):
    for i in range(len(bo)):
        if i%3 ==0  and i != 0:
            print("------------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j!= 0:
                print(" | ",end ="")

            if j== 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+ " ",end="")


def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] ==0:
                return (i,j) #row,column
    return None

def validCheck(bo,num,pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] !=i:
            return False
    # Check Box
    box1 = pos[1]//3
    box2 = pos[0]//3

    for i in range(box2*3,box2*3+3):
        for j in range(box1 *3, box1*3+3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def solveSudoku(bo):
    print(bo)
    find = findEmpty(bo)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if validCheck(bo,i,(row,col)):
            bo[row][col] = i
            if solveSudoku(bo):
                return True
            bo[row][col]= 0
    return False
printBoard(board)
solveSudoku(board)
print("\n Solution:  \n")
printBoard(board)