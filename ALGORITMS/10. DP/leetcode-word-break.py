# url :- https://leetcode.com/problems/word-break/

from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)
        del wordDict
        n = len(s)

        @lru_cache(maxsize=50000)
        def rec(i):
            if i == n :
                return True 
            
            curr = ''
            curr_ans = False
            for j in range(i, n):
                curr += s[j]
                print(i, curr)
                if curr in dictionary :
                    curr_ans = curr_ans or rec(j+1)    

            return curr_ans
        
        return rec(0)
        

sol = Solution()
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))