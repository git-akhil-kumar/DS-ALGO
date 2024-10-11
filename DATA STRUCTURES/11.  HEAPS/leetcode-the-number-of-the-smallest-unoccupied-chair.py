from heapq import heappop, heapify, heappush
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        times = [[v[0], v[1], i] for i, v in enumerate(times)]
        times.sort(key=lambda x: x[0])  
        chairs = list(range(n))
        heapify(chairs)
        processed = []

        for s, e, i in times:
            # Remove all the assigned chairs if their end time is less than or equal to current start time
            while processed and processed[0][0] <= s:
                _, chair = heappop(processed)
                heappush(chairs, chair)
            
            currChair = heappop(chairs)
            if i == targetFriend:
                return currChair
        
            heappush(processed, (e, currChair))
        return -1
    
sol = Solution()
print(sol.smallestChair([[1,4],[2,3],[4,6]], 1) == 1)
print(sol.smallestChair([[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]], 6) == 2)
