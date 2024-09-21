
def maximumGap(nums):
    n = len(nums)
    indexes = [i for i in range(n)]
    indexes = sorted(indexes, key=lambda i: nums[i])
    
    print(indexes)
    i, j = 0, 1
    max_gap = 0
    i = indexes[0]

    for j in indexes[1:]:
        if j > i :
            max_gap = max(max_gap, j - i)
        else :
            # start fresh window from "i"
            i = j
    return max_gap


print(maximumGap([3, 5, 4, 2]))

# 3 0 2 1