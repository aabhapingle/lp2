global n  # size of square board
global board  # 2 d array of board

n = int(input("Enter size: "))
board = []

# create board
for i in range(n):
    board.append([])
    for j in range(n):
        board[i].append(0)


# print board
def print_board():
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print('\n')


# check if queen is safe in this position
def check(row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


# solve the problem
def solve(col):
    if col >= n:  # base case
        return True
    for i in range(n):  # iterate over all rows
        if check(i, col):  # check if current position is safe
            board[i][col] = 1  # since it is safe, set to 1
            if solve(col+1):  # now that one col is fixed, see for further cols
                return True
            board[i][col] = 0  # backtracking step
    return False


print_board()
print(board)

if not solve(0):
    print('No solution exists')
else:
    print_board()