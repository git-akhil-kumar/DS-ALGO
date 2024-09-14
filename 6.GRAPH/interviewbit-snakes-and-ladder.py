# url :- https://www.interviewbit.com/problems/snake-ladder-problem/
# company tag :- Amazon 

# RULES:

# The game is played with cubic dice of 6 faces numbered from 1 to 6.
# Starting from 1 , land on square 100 with the exact roll of the die. If moving the number rolled would place the player beyond square 100, no move is made.
# If a player lands at the base of a ladder, the player must climb the ladder. Ladders go up only.
# If a player lands at the mouth of a snake, the player must go down the snake and come out through the tail. Snakes go down only.
# BOARD DESCRIPTION:

# The board is always 10 x 10 with squares numbered from 1 to 100.
# The board contains N ladders given in a form of 2D matrix A of size N * 2 where (A[i][0], A[i][1]) denotes a ladder that has its base on square A[i][0] and end at square A[i][1].
# The board contains M snakes given in a form of 2D matrix B of size M * 2 where (B[i][0], B[i][1]) denotes a snake that has its mouth on square B[i][0] and tail at square B[i][1].
#  Problem Constraints
# 1 <= N, M <= 15
# 1 <= A[i][0], A[i][1], B[i][0], B[i][1] <= 100
# A[i][0] < A[i][1] and B[i][0] > B[i][1]
# Neither square 1 nor square 100 will be the starting point of a ladder or snake.
# A square will have at most one endpoint from either a snake or a ladder.

# Input Format
# First argument is a 2D matrix A of size N * 2 where (A[i][0], A[i][1]) denotes a ladder that has its base on square A[i][0] and end at square A[i][1].
# Second argument is a 2D matrix B of size M * 2 where (B[i][0], B[i][1]) denotes a snake that has its mouth on square B[i][0] and tail at square B[i][1].
# Output Format
# Return the least number of rolls to move from start to finish on a separate line. If there is no solution, return -1.


from functools import cache


class Solution:
    def snakeLadder(self, ladders, snakes):
        moves = [1, 2, 3, 4, 5, 6]
        
        ladders_map = {}
        for x,y in ladders :
            ladders_map[x] = y
        del ladders
        snaker_map = {}
        for x, y in snakes :
            snaker_map[x] = y
        del snakes
            
        def isValid(step) :
            return step >= 1 and step <= 100    
        
        visited = set()
        @cache
        def dfs(curr_step) :
            if curr_step == 100 :
                return 0
            
            if curr_step > 100 or curr_step in visited:
                return float("inf")  # Invalid move
            
            visited.add(curr_step)

            curr_min = float("inf")
            for move in moves :
                next_step = curr_step + move
                
                if isValid(next_step) :
                    if next_step in ladders_map:
                        next_step = ladders_map[next_step]
                    
                    if next_step in snaker_map:
                        next_step = snaker_map[next_step]
                    
                    rec_ans = dfs(next_step)
                    if rec_ans != float("inf"):
                        curr_min = min(curr_min, 1 + rec_ans)
            visited.remove(curr_step)
            return curr_min
        
        ans = dfs(1)
        return ans
        
A = [[32, 62],[42, 68],[12, 98]]
B = [[95, 13],[97, 25],[93, 37],[79, 27],[75, 19],[49, 47],[67, 17]]

A1 = [ [8, 52],[6, 80],[26, 42],[2, 72]]
B1 = [ [51, 19],[39, 11],[37, 29],[81, 3],[59, 5],[79, 23],[53, 7],[43, 33],[77, 21]]

A2 = [[7, 98]]
B2 = [[99, 1]]

sol = Solution()
print(sol.snakeLadder(A, B) == 3)
print(sol.snakeLadder(A1, B1) == 5)
print(sol.snakeLadder(A2, B2) == 2)
