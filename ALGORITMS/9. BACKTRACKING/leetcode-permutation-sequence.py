class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(x) for x in range(1, n+1)]
        fact = 1
        
        for i in range(1, n):
            fact *= i

        ans = ""
        while True:
            ans += nums[k // fact] 

            if n == 0 :
                break

            k = k % fact  # type: ignore
            fact = fact // n
            n -= 1

        return ans
    
sol = Solution()
print(sol.getPermutation(4, 2))
"""

"""