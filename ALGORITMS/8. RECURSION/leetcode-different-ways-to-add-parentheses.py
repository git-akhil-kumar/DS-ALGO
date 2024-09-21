from typing import List


class Solution:
    

    def diffWaysToCompute(self, expression: str) -> List[int]:
        num = ''
        e = []
        for ch in expression:
            if ch in ['-','+','*']:
                e.append(num)
                e.append(ch)
                num = ''
            else :
                num += ch
        if num : 
            e.append(num)
        
        n = len(e)
        if n == 1 :
            return [int(e[0])]

        def compute(a, operator, b) :
            a = int(a)
            b = int(b)
            op = {"-": a - b, "+": a + b, '*': a * b}
            return str(op[operator])
                
        ans = []
        cache = set()

        def createCacheKey(arr):
            return "|".join(arr)

        def rec(curr):
            cacheKey = createCacheKey(curr)
            if cacheKey not in cache :
                # cache.add(cacheKey)
                n = len(curr)
                curr = curr[:]

                if n == 1 :
                    ans.append(int(curr[0]))
                    return 

                if n == 3 :
                    ans.append(int(compute(curr[0], curr[1], curr[2])))
                    return 
                
                for i in range(1, n-1, 2):
                    new_e = curr[0:i-1] + [compute(curr[i-1], curr[i], curr[i+1])] + curr[i+2:]
                    rec(new_e)     
        rec(e)
        print(ans)
        return ans


testcases = ["2-1-1","2*3-4*5","99","9-8+7-6+5-4","0+0+0+0+0*0+0+0*0+0","99*87-78+66*55-44+33","12+34-56*78+90","1+2-3+4-5+6-7+8-9+10"]
sol = Solution()
# print(sol.diffWaysToCompute("99") == [99])
print(sol.diffWaysToCompute("9-8+7-6+5-4") == [99])
# print(sol.diffWaysToCompute("2-1-1") == [0,2])
# print(sol.diffWaysToCompute("2*3-4*5") == [-34,-14,-10,-10,10])