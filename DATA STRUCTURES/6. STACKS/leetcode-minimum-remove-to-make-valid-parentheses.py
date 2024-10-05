# url : https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

from typing import Counter

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        res = ''
        c = Counter(s)
        op = c["("]
        cl = c[")"]

        for ch in s:
            if ch == '(' or ch == ')' :
                if ch == ')' :
                    if st and st[-1] == "(":
                        res += ch
                        st.pop()
                    cl -= 1
                if ch == '(':
                    if cl > 0 :
                        res += ch 
                        st.append('(')
                    cl -= 1 
            else :
                res += ch

        return res
        
tcs = ["lee(t(c)o)de)","a)b(c)d","))((","())()(((","(a(b(c)d)"]
res = ["lee(t(c)o)de","ab(c)d","","()()","a(b(c)d)"]

sol = Solution()
print()
for i, tc in enumerate(tcs):
    print(sol.minRemoveToMakeValid(tc), res[i])