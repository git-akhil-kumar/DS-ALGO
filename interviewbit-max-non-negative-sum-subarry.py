class Index :
    def __init__(self, i, j, s, l):
        self.start = i
        self.end = j
        self.arr_sum = s
        self.arr_len = l

class Solution:  
    def maxset(self, nums):
        n = len(nums)            
        index = Index(-1,-1, 0, 0)
        
        for i in range(n):
            curr_len = 0
            curr_sum = 0
            start = i
            while i < n and nums[i] >= 0 :
                curr_sum += nums[i]
                curr_len += 1
                i += 1
                
            if curr_sum >= index.arr_sum :
                print(curr_sum, start, i, index)
                if curr_sum > index.arr_sum :
                    index.start = start 
                    index.end = i - 1
                    index.arr_sum = curr_sum
                    index.arr_len = curr_len
                    
                elif curr_sum == index.arr_sum and curr_len > index.arr_len :
                    index.start = start
                    index.end = i - 1
                    index.arr_len = curr_len
                        
        return nums[index.start:index.end+1]

sol = Solution()
print(sol.maxset([ 0, 0, -1, 0 ]))