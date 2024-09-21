from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window = [0] * (n+1)
        window[0] = 1
        total_odds = 0
        ans = 0
        for i in range(n) :
            total_odds += nums[i] & 1 
            if total_odds >= k :
                ans += window[total_odds - k]
            window[total_odds] += 1
        return ans
    
sol = Solution()
print(sol.numberOfSubarrays([1,1,2,1,1], 3) == 2)
print(sol.numberOfSubarrays([2,4,6], 1) == 0)
print(sol.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2) == 16)
print(sol.numberOfSubarrays([2,2,2,1], 1) == 4)
