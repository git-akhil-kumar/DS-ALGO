
from typing import Counter


class Solution:
    def findOccurences(self, nums):
        counter = list(Counter(nums).items())
        counter.sort(key=lambda x: x[0])
        return [freq for vals, freq in counter]
    
sol = Solution()
print(sol.findOccurences( [4, 3, 3]))