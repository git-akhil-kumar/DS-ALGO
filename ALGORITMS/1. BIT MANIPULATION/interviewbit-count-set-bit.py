class Solution:
    def solve(self, n):
        cnt = 1
        for i in range(2, n+1) :
            k = 0
            while i > 0 :
                cnt += i & 1 
                i = i >> 1
        return cnt



sol = Solution()
print(sol.solve(3) == 4)
print(sol.solve(1) == 1)
print(sol.solve(10000000) == 114434632)