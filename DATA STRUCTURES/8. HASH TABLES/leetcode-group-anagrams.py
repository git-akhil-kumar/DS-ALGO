# url :- https://leetcode.com/problems/group-anagrams/
 

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            l = list(s)
            l.sort()
            key = "".join(l)

            if key in res :
                res[key].append(s)
            else :
                res[key] = [s]
        ans = []
        for _,v in res.items():
            ans.append(v)
        
        return ans
        