class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2 :
            return False
        
        window = [0] * 26

        s1_chars = [0] * 26
        for ch in s1:
            ch_idx = ord(ch) - ord('a')
            s1_chars[ch_idx] += 1
        
        def check(window):
            for i in range(26):
                if s1_chars[i] != window[i]:
                    return False
            return True

        for i in range(n2):
            ch = s2[i]
            ch_idx = ord(ch) - ord('a')
            if i < n1-1:
                window[ch_idx] += 1
            else:
                window[ch_idx] += 1
                if check(window):
                    return True
                last_chr = s2[i-n1+1] 
                last_chr_idx = ord(last_chr) - ord('a')
                window[last_chr_idx]-=1
            
        return False
    
sol = Solution()
print(sol.checkInclusion("ab", "eidboaoo"))
print(sol.checkInclusion("ab", "eidbaooo"))
