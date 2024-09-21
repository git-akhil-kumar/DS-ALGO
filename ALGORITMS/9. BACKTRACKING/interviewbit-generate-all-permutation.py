
def permute(nums):
    ans = []
    n   = len(nums)
    def backtracking(i, nums):
        if i == n :
            ans.append(nums[:])
            return 
        
        for k in range(i, n):
            nums[i], nums[k] = nums[k], nums[i]
            backtracking(i+1, nums)
            nums[i], nums[k] = nums[k], nums[i]
        
    backtracking(0, nums)
    del nums
    return ans

nums=[1,2,3]
print(permute(nums))
