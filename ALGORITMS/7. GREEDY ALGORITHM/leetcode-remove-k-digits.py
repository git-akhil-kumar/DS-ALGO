# url :- https://leetcode.com/problems/remove-k-digits/

from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num) :
            return "0"
        
        if len(num) <= 1:
            return num
        
        n = len(num)
        stack = []
    
        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                k -= 1
                stack.pop()
            
            stack.append(ch)

        stack = stack[:len(stack) - k]
        res = ""
        last = True 
        for ch in stack :
            if ch == '0' and last :
                continue
            if ch != '0' :
                last = False 
            res += ch 
        return res

    
sol = Solution()
print(sol.removeKdigits("1432219", 3) == '1219')
print(sol.removeKdigits("10200", 1) == '200')
print(sol.removeKdigits("10", 2) == "0")   