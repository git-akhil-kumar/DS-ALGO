# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens’ placement, 
# where 'Q' and '.' both indicate a queen and an empty space respectively.
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

def solveNQueens(n):
    diagonals = [(-1, 1), (1, -1), (1, 1), (-1, -1)]

    board = [['.' for _ in range(n)] for _ in range(n)]

    def checkDiagonals(r, c):
        row , col = r + diagonals[0][0], c + diagonals[0][1]
        while isValid(row, col):
            if board[row][col] == 'Q' :
                return False
            row , col = row + diagonals[0][0], col + diagonals[0][1]

        row, col = r + diagonals[1][0], c + diagonals[1][1]
        while isValid(row, col):
            if board[row][col] == 'Q' :
                return False
            row , col = row + diagonals[1][0], col + diagonals[1][1]

        row , col = r + diagonals[2][0], c + diagonals[2][1]
        while isValid(row, col):
            if board[row][col] == 'Q' :
                return False
            row , col = row + diagonals[2][0], col + diagonals[2][1]

        row , col = r + diagonals[3][0], c + diagonals[3][1]
        while isValid(row, col):
            if board[row][col] == 'Q' :
                return False
            row , col = row + diagonals[3][0], col + diagonals[3][1]

        return True

    def isValid(row, col):
        return row >= 0 and row < n and col >= 0 and col < n 

    cols = set()
    ans = []
    queens = 0

    def backtrack(row):
        nonlocal queens

        if row == n and queens == n:
            curr_board = ["".join(board[i]) for i in range(n)]
            ans.append(curr_board)
            return 
        for col in range(n):
            if col not in cols and checkDiagonals(row, col):
                board[row][col] = 'Q'
                cols.add(col)
                queens += 1
                backtrack(row+1)

                board[row][col] = '.'
                cols.remove(col)
                queens -= 1

    backtrack(0)
    return ans


boards = solveNQueens(4)
for board in boards :
    print("-----------------")
    for row in board :
        print(row)
