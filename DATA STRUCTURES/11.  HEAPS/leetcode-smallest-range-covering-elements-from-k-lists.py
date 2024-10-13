from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minQ = []
        max_ele = -float("inf")

        n = len(nums)
        for i in range(n):
            heappush(minQ, (nums[i][0],  i, 0))
            max_ele = max(max_ele, nums[i][0])

        min_ele = minQ[0][0]
        res = [min_ele, max_ele]
        
        while True:
            min_ele, row, col = heappop(minQ)

            if col == len(nums[row]) - 1:
                break
            
            col += 1
            next_ele = nums[row][col]
            heappush(minQ, (next_ele, row, col))
            max_ele = max(max_ele, next_ele)
    
            min_ele, _, _ = minQ[0]

            if (max_ele - min_ele) < (res[1] - res[0]):
                res = [min_ele, max_ele]

        return res

sol = Solution()
print(sol.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]) == [20, 24])

        

# [4,10,15,24,26] [0,9,12,20] [5,18,22,30] 0, 5.  heap [0,4,5]
# [4,10,15,24,26] [9,12,20] [5,18,22,30] 4, 9 => heap [4,5,9]
# [10,15,24,26] [9,12,20] [5,18,22,30] 5, 10. => heap [5,9,10]
# [10,15,24,26] [9,12,20] [18,22,30] 9, 18 => heap[9,10,18]
# [10,15,24,26] [12,20] [18,22,30] 10, 18 
# [15,24,26] [12,20] [18,22,30] 12, 18
# [24,26] [20] [18,22,30] 18, 24
# [24,26] [20] [22,30] 20, 24
# [24,26] [] [22,30]  stop