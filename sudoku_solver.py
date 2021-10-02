#Adam Dubsky
#Program that solves unfinished sudoku puzzle
#Program primarily used recursion through backtracking


#function that checks to see if the change is valid
def valid_move(board, number, column, row):
    #Checks row
    for x in range(9):
        if board[row][x] == number:
            return False

    #Checks column
    for x in range(9):
        if board[x][column] == number:
            return False

    #finds the top left row and column
    top_left_row = row - row % 3
    top_left_column = column - column % 3

    #Checks for the same number in teh same row and column (3 X 3 field)
    for x in range(3):
        for y in range(3):
            if board[top_left_row + x][top_left_column + y] == number:
                return False

    return True

#backtracking function that solves the board using recursion
def recurs_solve(board, row, column):
    #checks for overflow in column/row which means solution found
    if column == 9:
        if row == 8:
            return True

        row += 1
        column = 0

    if board[row][column] > 0:
        return recurs_solve(board, row, column + 1)

    for num in range (1,10):
        if valid_move(board, num, column, row):
            board[row][column] = num
            #indicates a solution
            if recurs_solve(board, row, column + 1):
                return True

        board[row][column] = 0
    return False

#set board variable as a list
board = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
         [0, 0, 0, 0, 7, 3, 0, 0, 9],
         [3, 0, 9, 0, 0, 0, 0, 4, 5],
         [4, 9, 0, 0, 0, 0, 0, 0, 0],
         [8, 0, 3, 0, 5, 0, 9, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 3, 6],
         [9, 6, 0, 0, 0, 0, 3, 0, 8],
         [7, 0, 0, 6, 8, 0, 0, 0, 0],
         [0, 2, 8, 0, 0, 0, 0, 0, 0]]

#Calls functions and outputs the solution to the sudoku
if recurs_solve(board, 0, 0):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
else:
    print("No Solution Found ")
