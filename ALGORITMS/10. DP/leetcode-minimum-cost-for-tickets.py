from bisect import bisect_left, bisect_right
from functools import lru_cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)     
        plans = {0:1, 1:7, 2:30}

        @lru_cache(None)
        def rec(i: int) :
            if i >= n :
                return 0 

            min_cost = 10**10-1 
            for index, cost in enumerate(costs):
                nextIndex = bisect_right(days, days[i] + plans[index] - 1)
                if nextIndex < n :
                    min_cost = min(min_cost, cost + rec(nextIndex))
                else :
                    min_cost = min(min_cost, cost)
                
            return min_cost
        
        return rec(0)


sol = Solution()
print(sol.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2, 7, 15]))
print(sol.mincostTickets([1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28], [3,13,45]))
print(sol.mincostTickets([3,5,6,8,9,10,11,12,13,14,15,16,20,21,23,25,26,27,29,30,33,34,35,36,38,39,40,42,45,46,47,48,49,51,53,54,56,57,58,59,60,61,63,64,67,68,69,70,72,74,77,78,79,80,81,82,83,84,85,88,91,92,93,96], [3,17,57]))
            
