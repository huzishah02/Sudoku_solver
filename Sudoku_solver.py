board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



def solve(bo):
    #Base Case
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0 #Backtrack and reset the value

    return False




def valid(bo, num, pos):
    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
                   
    #Check Column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
                   
    #Check Box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):         #Looping through each box 
          for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True               


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0: #for every columns after every 3 numbers down we print a border.
            print("- - - - - - - - - - - - - ")

        for j in range (len(bo[0])): 
            if j % 3== 0 and j != 0: # After every 3rd number to the right we get a border and no border is printed to the left of the board
                print (" | ", end="") 
                
            if j == 8: #check to see if we are at the last position
                print(bo[i][j]) 
            else:
                print(str(bo[i][j]) + ' ', end="") #end="" means to stay on the same line


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0: 
                return (i, j) #row, col

    return None


#print_board(n_board)
#solve(n_board)
#print("__________________")
#print_board(n_board)


#print("Unsolved Sudoku:")
#print_board(n_board)
#solve(n_board)
#rint("\nSolved Sudoku:")
#rint_board(n_board)

print("Initial Sudoku Board:")
print_board(board)
if solve(board):
    print("Sudoku Board Solved:")
    print_board(board)
else:
    print("No solution exists for the given Sudoku board.")
 