
def sortColors(nums):
    n = len(nums)
    if n == 0 or n == 1 :
        return nums
    start, i, end = 0, 0, n-1    
    while i <= end :
        if nums[i] == 0 :
            nums[start], nums[i] = nums[i], nums[start]
            start += 1
            i += 1
        elif nums[i] == 1 :
            i += 1    
        elif nums[i] == 2 :
            nums[i], nums[end] = nums[end], nums[i]
            end -= 1
    return nums

print(sortColors([ 0, 2, 2, 0, 0, 2, 1, 2, 0, 1, 1, 2, 0, 2, 2, 0, 1, 0, 0, 1, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 1, 0, 2, 2, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 2, 0, 1, 0, 2, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 2, 1, 0, 2, 1, 0, 2, 0, 0, 2, 2, 1, 2, 2, 2, 1, 0, 0, 0, 2, 2, 1, 0, 1, 1, 0, 2, 0, 1, 2, 2, 2, 0, 2, 1, 0, 1, 2, 0, 2, 2, 0, 2, 1, 1, 2, 1, 2, 0, 2, 2, 2, 1, 2, 0, 1, 1, 1, 0, 1, 0, 1, 2, 2, 1, 1, 0, 2, 2, 1, 2, 2, 1, 0, 0, 0, 1, 1, 1, 2, 0, 2, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 2, 1, 1, 1, 2, 0, 2, 0, 2, 0, 0, 0, 1, 1, 0, 1, 2, 0, 2, 1, 0, 0, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0, 1, 2, 2, 1, 0, 1, 2, 0, 1, 0, 2, 2, 0, 0, 1, 1, 1, 0, 0, 0, 2, 2, 2, 0, 2, 1, 0, 1, 2, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 1, 2, 0, 1, 0, 1, 2, 1, 2, 0, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 2, 1, 2, 0, 2, 1, 1, 0, 1, 0, 2, 1, 2, 2, 1, 2, 0, 0, 2, 0, 0, 2, 0, 0, 1, 2, 0, 0, 0, 1, 0, 2, 1, 0, 1, 0, 1, 2, 0, 2, 0, 1, 1, 2, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 2, 2, 2, 0, 0, 1, 1, 2, 0, 0, 0, 1, 2, 1, 2, 2, 0, 0, 1, 0, 2, 0, 2, 1, 2, 1, 2, 2, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 2 ]))