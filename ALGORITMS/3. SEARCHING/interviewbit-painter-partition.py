class Solution:
    def paint(self, total_painters, time_to_paint, boards):
        def isPossible(time_to_finish) :
            painter = 1
            curr_time = 0
            for board in boards : 
                curr_time += board * time_to_paint
                
                if curr_time > time_to_finish :
                    curr_time = board * time_to_paint
                    painter += 1
                    if painter > total_painters :
                        return False
            return True
        
        left = max(boards) * time_to_paint
        right = sum(boards) * time_to_paint 
        
        while left <= right : 
            mid = left + (right - left) // 2
            
            if isPossible(mid) :
                ans = mid 
                right = mid - 1
            else :
                left = mid + 1
            
        return ans % 10000003
    
sol = Solution()
print(sol.paint(3, 10, [ 640, 435, 647, 352, 8, 90, 960, 329, 859 ]))