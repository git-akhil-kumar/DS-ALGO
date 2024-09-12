# url :- https://www.interviewbit.com/problems/maximal-string/
# company tag :- facebook, apple
# description :- Given a string A and integer B, what is maximal lexicographical string 
# that can be made from A if you do atmost B swaps.
# Problem Constraints
# 1 <= |A| <= 9
# A contains only digits from 0 to 9.
# 1 <= B <= 5

# Solution approach :- 
# 1. we will use backtracking to generate all possible permutations of the string A.
# 2. we need to take care that if the current character is already the maximum in the remaining string, we should not swap it.
# 3. if the current character is not the maximum, we will swap it with the maximum character in the remaining string.
# 4. we will keep track of the maximum lexicographical string that can be made from A.
# 5. we will use a helper function to check if the current string is lexicographically greater than the maximum string.
# 6. if it is, we will update the maximum string.

def maximalString(stringA, max_swap_allowed):
    max_str = int(stringA)
    n = len(stringA)
    def backtracking(i, curr_str, swaps_left):
        nonlocal max_str
        curr_str_converted_to_int = "".join(curr_str)
        max_str = max(max_str, int(curr_str_converted_to_int))

        if swaps_left == 0 or i == n :
            return
        
        if curr_str[i] == max(curr_str[i:]):
            backtracking(i+1, curr_str, swaps_left)
        else :    
            for j in range(i, n):
                if curr_str[j] == max(curr_str[j:]) :
                    curr_str[i], curr_str[j] = curr_str[j], curr_str[i]
                    backtracking(i+1, curr_str, swaps_left-1)
                    curr_str[i], curr_str[j] = curr_str[j], curr_str[i]

    string_in_arr = [ch for ch in stringA]
    del stringA
    backtracking(0, string_in_arr, max_swap_allowed)
    return max_str

isPassed = maximalString("254", 1) == 524  and \
            maximalString("254", 2) == 542 and \
            maximalString("129814999", 4) == 999984211 
            
print(isPassed)