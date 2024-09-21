def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j  # Pattern found
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1
    
    return -1  # Pattern not found

# Example usage
text = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB"
pattern = "AAB"
result = kmp_search(text, pattern)
print(f"Pattern found at index: {result}")