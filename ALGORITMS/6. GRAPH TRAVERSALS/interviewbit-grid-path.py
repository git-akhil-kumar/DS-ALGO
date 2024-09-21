from functools import cache, lru_cache
from typing import Counter


class Solution:
    def gridPath(self, matrix):
        n, m = len(matrix), len(matrix[0])
        
        if not matrix or not matrix[0] or matrix[n-1][m-1] == 0 or matrix[0][0] == 0 :
            return 0
        
        movements = [(0,-1),(0,1),(1,0),(-1,0)]
        
        zeroes = sum(row.count(0) for row in matrix)
        N = n ** 2 - zeroes

        def isValid(x, y):
            nonlocal n,m
            return x >= 0 and x < n and y >= 0 and y < m and matrix[x][y] != 0
        
        visited = [[False for _ in range(n)] for _ in range(m)]

        paths = []

        def dfs(x, y, step, curr_path) :

            if x == n - 1 and y == m - 1 and step == N :
                curr_path.append(matrix[x][y])
                paths.append(curr_path[:])
                visited[x][y] = False
                curr_path.pop()
                return 
            
            visited[x][y] = True 
            curr_path.append(matrix[x][y])

            for dx, dy in movements :
                nx = x + dx 
                ny = y + dy 
                
                if isValid(nx, ny) and not visited[nx][ny] :
                    dfs(nx, ny, 1 + step, curr_path)

            visited[x][y] = False
            curr_path.pop()

        dfs(0, 0, 1, []) 
        ans = 0
        for path in paths:
            for i in range(1, len(path)) :
                ans += abs(path[i] - path[i-1])
        return ans
            

    def optimisedGridPath(self, matrix) :
        n = len(matrix)
        movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_cost = 0
        zeroes = sum(row.count(0) for row in matrix)
        N = n * n - zeroes

        def isValid(x, y, visited):
            return 0 <= x < n and 0 <= y < n and matrix[x][y] != 0 and not visited[x][y]
        
        def dfs(x, y, step, prev_val, visited):
            nonlocal total_cost
            if x == n - 1 and y == n - 1 and step == N:
                return 0
            
            visited[x][y] = True
            path_cost = 0

            for dx, dy in movements:
                nx, ny = x + dx, y + dy
                if isValid(nx, ny, visited):
                    step_cost = abs(matrix[nx][ny] - prev_val)
                    path_cost += step_cost + dfs(nx, ny, step + 1, matrix[nx][ny], visited)

            visited[x][y] = False
            return path_cost

        visited = [[False] * n for _ in range(n)]
        return dfs(0, 0, 1, matrix[0][0], visited)

sol = Solution()
print(sol.optimisedGridPath([[5,2],[0,7]]) == 8)
print(sol.optimisedGridPath([[79, 19, 59],[45, 89, 63],[79, 81, 37]]) == 472)
print(sol.optimisedGridPath([[45, 15, 14, 16, 30, 24],[56, 13, 55, 3, 0, 40],[14, 36, 1, 76, 94, 54],[91, 81, 75,\
                            18, 57, 86],[92, 97, 51, 87, 46, 100],[16, 44, 11, 46, 23, 36]]) == 722618)
print(sol.optimisedGridPath([[81, 33, 91, 98, 10, 71, 21],[9, 15, 62, 88, 1, 50, 80],[24, 70, 48, 36, 80, 41, 10],\
                             [72, 98, 15, 80, 86, 61, 12],[12, 21, 31, 34, 26, 63, 22],[47, 35, 100, 13, 89, 26, 54],[35, 73, 48, 51, 68, 69, 9]]) == 192835542)
            
 
                    