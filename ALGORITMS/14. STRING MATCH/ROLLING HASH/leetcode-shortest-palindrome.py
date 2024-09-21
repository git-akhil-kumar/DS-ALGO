# url :- https://leetcode.com/problems/shortest-palindrome/description/
# description :- You are given a string s. You can convert s to a palindrome
#  by adding characters in front of it. Return the shortest palindrome you can 
# find by performing this transformation.
# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of lowercase English letters only.

# Approach :- 


import string
from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n          = len(s)
        last_index = 0
        prefix     = 0
        suffix     = 0
        base       = 37 
        power      = 1

        for i, ch in enumerate(s):
            char   = ord(ch) - ord('a') + 1
            prefix = prefix * base + char
            suffix = char * power + suffix
            
            if prefix == suffix : 
                last_index = i

        suffix = s[last_index+1:]

        return suffix[::-1] + s
        
sol = Solution()
print(sol.shortestPalindrome("aabaa"))