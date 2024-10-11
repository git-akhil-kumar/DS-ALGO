from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        stack = []
        n = len(nums)
        stack.append(nums[n-1])
        for i in range(n-2, -1, -1):
            if nums[i] > stack[-1]:
                stack.append(nums[i])

        while r < n :
            while l < r and stack and stack[-1] >= nums[l]:
                l += 1
                stack.pop()
            res = max(res, r-l)
            r += 1


            
        return res
        


sol = Solution()
print("----------------------------------")
print(sol.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))