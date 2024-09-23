# url : https://leetcode.com/problems/extra-characters-in-a-string/

from functools import lru_cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)
        del dictionary

        @lru_cache(None)
        def rec(i):
            if i == n :
                return 0    

            curr_min = n
            curr = ""
            for j in range(i,n):
                curr += s[j]
                if curr in dictionary_set :
                    curr_min = min(curr_min, rec(j+1))
                else :
                    curr_min = min(curr_min, len(curr) + rec(j+1))

            return curr_min

        return rec(0)


sol = Solution()
# print(sol.minExtraChar("sayhelloworld", ["hello","world"]))
# print(sol.minExtraChar("dwmodizxvvbosxxw",["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]))
print(sol.minExtraChar("xp", ["a","u","d","b","s","r","z","y","f","l","q","i","j","w","o","c"]))
        

        