def permute(nums):
    nums_set = set()
    n    = len(nums)
    ans  = []
    def backtrack(i, nums):
        if i == n :
            curr_set_str = ','.join(str(x) for x in nums)
            if curr_set_str not in nums_set :
                ans.append(nums[:])
                nums_set.add(curr_set_str)
            return 
            
        for j in range(i, n):
            nums[i], nums[j] = nums[j], nums[i]
            backtrack(i+1, nums)
            nums[i], nums[j] = nums[j], nums[i]
    
    backtrack(0, nums)
    del nums
    return ans        
print(permute([1 ,2, 3]))

