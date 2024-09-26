# url :- https://leetcode.com/problems/furthest-building-you-can-reach
from heapq import heappush, heappop
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)

        for i in range(n-1):
            if heights[i] < heights[i+1]:
                diff = heights[i+1] - heights[i]

                heappush(heap, diff)

                if len(heap) > ladders:
                    bricks -= heappop(heap)

                if bricks < 0 :
                    return i
                    
        return n-1
    

sol = Solution()
print(sol.furthestBuilding([4,2,7,6,9,14,12], 5, 1) == 4)
print(sol.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2) == 7)
print(sol.furthestBuilding([14,3,19,3], 17, 0) == 3)
