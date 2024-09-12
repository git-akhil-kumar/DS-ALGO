def AllParenthesis(n):
    # code here
    length, ans = 2 * n, []

    def backtracking(opened, closed, curr):
        if opened >= n and closed >= n:
            if len(curr) == length:
                ans.append(curr[:])
            return

        if opened > closed:
            backtracking(opened, closed + 1, curr + ")")

        if opened < n :
            backtracking(opened + 1, closed, curr + "(")

    backtracking(0, 0, "")
    return ans


results = AllParenthesis(4)
for res in results:
    print(res)
