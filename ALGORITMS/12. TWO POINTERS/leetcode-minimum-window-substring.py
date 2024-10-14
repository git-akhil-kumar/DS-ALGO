from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if n < m :
            return ""
        res = ""
        res_length = float("inf")
        count = Counter(t)
        window = [0]*256
        l, r = 0, 0
        def isWindowValid(window, word):
            
            verdict = True
            for k, v in count.items():
                i = ord(k)
                if window[i] < count[k]:
                    verdict = False
                    break
            # print(word, verdict)
            return verdict
        while r<n:
            i = ord(s[r])
            window[i] += 1

            while l <= r and isWindowValid(window, s[l:r+1]):
                if r-l+1 < res_length:
                    res_length = r-l+1
                    res = s[l:r+1]
                i = ord(s[l])
                window[i] -= 1
                l += 1
            
            r += 1
        return res 
        

sol = Solution()
print(sol.minWindow("ab","A"))