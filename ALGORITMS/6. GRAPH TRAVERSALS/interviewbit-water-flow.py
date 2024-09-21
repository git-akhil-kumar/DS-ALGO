# url :- https://www.interviewbit.com/problems/water-flow/
# same as leetcode :- https://leetcode.com/problems/pacific-atlantic-water-flow/description/

class Solution:
    def waterFlow(self, heights):
        
        if not heights or not heights[0] :
            return []
            
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(heights), len(heights[0])
        
        def isValid(x, y) :
            nonlocal n,m 
            return x >= 0 and x < n and y >= 0 and y < m 
            
        blue = [[False for _ in range(m)] for _ in range(n)]
        red = [[False for _ in range(m)] for _ in range(n)]
        
        def dfs(i, j, lake) :
            lake[i][j] = True 
            
            for di, dj in movements :
                ni, nj = i + di, j + dj 
                
                if isValid(ni, nj) and not lake[ni][nj] and heights[ni][nj] >= heights[i][j] :
                    dfs(ni, nj, lake)

        for i in range(n):
            dfs(i, 0, blue)
            dfs(i, m-1, red)
        
        for i in range(m): 
            dfs(0, i, blue)
            dfs(n-1, i, red)
            
        cnt = 0
        for i in range(n) :
            for j in range(m) :
                if blue[i][j] and red[i][j] :
                    cnt += 1
        return cnt   
        
        

sol = Solution()
print(sol.waterFlow([[1, 2, 2, 3, 5],[3, 2, 3, 4, 4],[2, 4, 5, 3, 1],[6, 7, 1, 4, 5],[5, 1, 1, 2, 4]]) == 7)
print(sol.waterFlow([[2, 2],[2, 2]]) == 4)
print(sol.waterFlow([[1,2,3],[4,0,5],[6,7,8]]) == 5)