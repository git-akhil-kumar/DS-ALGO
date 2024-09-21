# url :- https://www.interviewbit.com/problems/sudoku/
# company tag :- Microsoft
# difficulty  :- MEDIUM-HARD

# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.' You may assume that there will be only one unique solution.
# Note: You must update the input argument A (partially completed grid of Sudoku) to submit your solved Sudoko grid.
# Example :
# For the above given diagrams, the corresponding input to your program will be

# [[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
# and we would expect your program to modify the above array of array of characters to

# [[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]



class Solution:
    def solveSudoku(self, board):
        board = [list(row) for row in board]

        def check(x, y, ch):
            for i in range(9):
                if board[x][i] == ch or board[i][y] == ch :
                    return False 
            
            row_start = ( x // 3 ) * 3
            col_start = ( y // 3 ) * 3

            for row in range(row_start, row_start + 3) :
                for col in range(col_start, col_start + 3) :
                    if board[row][col] == ch :
                        return False 
            
            return True
        
        def dfs(row, col) :
            if row == 9 :
                return True
            
            if col == 9 :
                return dfs(row + 1, 0)
            
            if board[row][col] != '.' :
                return dfs(row, col+1)
            
            if board[row][col] == '.' :
                for ch in range(1, 10):
                    if check(row, col, str(ch)) :
                        board[row][col] = str(ch)
                        if dfs(row, col + 1) : 
                            return True
                        else :
                            board[row][col] = '.'
            return False

        dfs(0, 0)
        for row in board:
            print("".join(row))
        

sol = Solution()
sol.solveSudoku([ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ])