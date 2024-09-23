from math import ceil, floor, log2
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        m = (2 ** n)
        nums_set = set(nums)
        first = '0' * n
        if first not in nums_set :
            return first
        
        for i in range(1, m):
            str = ""
            temp = i
            # Convert decimal number to binary number
            while temp:
                if temp & 1:
                    str = "1" + str
                else:
                    str = "0" + str
                temp >>= 1 

            if len(str) < n :
                str = "0" * (n-len(str)) + str 

            if str not in nums_set :
                return str
        return " "

sol = Solution()

print(sol.findDifferentBinaryString(["00","01"]))




"""
0   ->   0000
1   ->   0001
2   ->   0010
3   ->   0011
4   ->   0100
5   ->   0101
6   ->   0110
7   ->   0111
8   ->   1000
9   ->   1001
10  ->   1010
11  ->   1011
12  ->   1100
13  ->   1101
14  ->   1110
15  ->   1111
16  ->  10000


"""