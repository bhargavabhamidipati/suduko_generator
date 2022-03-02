import random
'''
    1. The board is initialised with zeros initially.
    2. A random square is selected from the available nine squares.
    3. This square is solved for all the numbers from one to nine.
    4. The board obtained from step 3 is passed to solve function.
    5. Now randomly a number is chosen between 35 to 45, which is
       the number of empty spaces that are required in the generated
       board.
    6. Now randomly the elements are replaced with zeros thus obtaining
       the sudoku puzzle.
'''

bo = [[0 for i in range(9)] for j in range(9)]

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return None

def solve(bo):
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

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def generate(bo):
    num = random.randint(0,8)
    values = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    choosen = values[num]
    set_values = []
    for i in range(3):
        for j in range(3):
            num=random.randint(1,9)
            while num in set_values:
                num = random.randint(1,9)
            bo[choosen[0]+i][choosen[1]+j] = num
            set_values.append(num)

def generate_puzzle(bo):
    generate(bo)
    solve(bo)
    no_values = random.randint(35,45)
    set_values = []
    for i in range(0,no_values):
        x = random.randint(0,8)
        y = random.randint(0,8)
        while (x,y) in set_values:
            x = random.randint(0,8)
            y = random.randint(0,8)
        bo[x][y] = 0
        set_values.append((x,y))



print("                  PUZZLE BOARD")
print("__________________________________________________\n")
generate_puzzle(bo)
print_board(bo)
print("                     SOLUTION")
print("__________________________________________________\n")
solve(bo)
print_board(bo)

