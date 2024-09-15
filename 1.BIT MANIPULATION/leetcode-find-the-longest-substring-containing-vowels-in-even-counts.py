# url :- https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
# difficulty :- HARD
# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
# Example 1:
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
# Example 2:
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
# Example 3:
# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

# Constraints:
# 1 <= s.length <= 5 x 10^5
# s contains only lowercase English letters.


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels_map = {"a":0,"e":0,"i":0,"o":0,"u":0}
        cache = {"00000": -1}
        ans = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in vowels_map :
                vowels_map[ch] = ( vowels_map[ch] + 1 ) % 2
            curr_state = ""

            for _, v in vowels_map.items():
                curr_state += str(v)

            if curr_state in cache :
                ans = max(ans, i - cache[curr_state])
            else :
                cache[curr_state] = i
        
        return ans

    def findTheLongestSubstingUsingBitMask(self, s) -> int:
        vowels_map = {"a":16,"e":8,"i":4,"o":2,"u":1}
        curr_state = 0
        ans = 0
        cache = {}
        cache[0] = -1
        for i in range(len(s)):
            ch = s[i]
            if ch in vowels_map:
                curr_state = curr_state ^ vowels_map[ch] 
            if curr_state in cache :
                ans = max(ans, i - cache[curr_state])
            else :
                cache[curr_state] = i
        return ans
    
sol = Solution()
print(sol.findTheLongestSubstingUsingBitMask("elee") == 3)
print(sol.findTheLongestSubstingUsingBitMask("eleetminicoworoep") == 13)
print(sol.findTheLongestSubstingUsingBitMask("leetcodeisgreat") == 5)
print(sol.findTheLongestSubstingUsingBitMask("bcbcbc") == 6)
