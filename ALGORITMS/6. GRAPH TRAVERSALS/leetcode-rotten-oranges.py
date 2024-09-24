# url :- https://leetcode.com/problems/rotting-oranges

# Approach :- multi source bfs 
# TC :- O(n * m)
# SC :- O(n * m) i.e queue size 

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        n, m = len(grid), len(grid[0])
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        if len(queue) == 0:
            return -1
        
        movements = [[0,1],[0,-1],[1,0],[-1,0]]

        def isValid(i, j):
            return i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == 1
        
        time = 0
        while len(queue) > 0 :
            size = len(queue)
            time += 1
            for i in range(size):       
                row, col = queue.popleft()
                for move_row, move_col in movements:

                    next_row = row + move_row
                    next_col = col + move_col

                    if isValid(next_row, next_col) :
                        grid[next_row][next_col] = 2
                        fresh -= 1
                        if fresh == 0 :
                            return time
                        queue.append((next_row, next_col))
                    
                
        return time if fresh == 0 else -1

sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4)
print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1)
print(sol.orangesRotting([[0,2]]) == 0)
print(sol.orangesRotting([[0]]) == 0)
