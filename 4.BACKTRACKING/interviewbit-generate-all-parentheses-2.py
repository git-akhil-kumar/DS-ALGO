# link :- https://www.interviewbit.com/problems/generate-all-parentheses-ii/
# company tag :- amazon, microsoft, bloomberg, facebook, google


def generateParenthesis(n):
    ans = []
    def bactracking(opened, closed, curr) :
        if closed == n :
            ans.append(curr[:])

        if opened < n :
            print('before open', opened + 1, closed, curr + '(')
            bactracking(opened + 1, closed, curr + '(')
            print('after open', opened + 1, closed, curr + '(')

        if closed < opened :
            print('before closed', opened, closed + 1, curr + ')')
            bactracking(opened, closed + 1, curr + ')')
            print('after closed', opened, closed + 1, curr + ')')
    
    bactracking(0, 0, "")
    return ans


print(generateParenthesis(3))




"""
╭─----------------------------------------------─╮
|   Recursion tree with closing condition first  |
╰─----------------------------------------------─╯
before open 1 0 (
before closed 1 1 ()
before open 2 1 ()(
before closed 2 2 ()()
before open 3 2 ()()(
before closed 3 3 ()()()
after closed 3 3 ()()()
after open 3 2 ()()(
after closed 2 2 ()()
before open 3 1 ()((
before closed 3 2 ()(()
before closed 3 3 ()(())
after closed 3 3 ()(())
after closed 3 2 ()(()
after open 3 1 ()((
after open 2 1 ()(
after closed 1 1 ()
before open 2 0 ((
before closed 2 1 (()
before closed 2 2 (())
before open 3 2 (())(
before closed 3 3 (())()
after closed 3 3 (())()
after open 3 2 (())(
after closed 2 2 (())
before open 3 1 (()(
before closed 3 2 (()()
before closed 3 3 (()())
after closed 3 3 (()())
after closed 3 2 (()()
after open 3 1 (()(
after closed 2 1 (()
before open 3 0 (((
before closed 3 1 ((()
before closed 3 2 ((())
before closed 3 3 ((()))
after closed 3 3 ((()))
after closed 3 2 ((())
after closed 3 1 ((()
after open 3 0 (((
after open 2 0 ((
after open 1 0 (
['()()()', '()(())', '(())()', '(()())', '((()))']

╭─----------------------------------------------─╮
|   Recursion tree with opening condition first  |
╰─----------------------------------------------─╯
before open 1 0 (
before open 2 0 ((
before open 3 0 (((
before closed 3 1 ((()
before closed 3 2 ((())
before closed 3 3 ((()))
after closed 3 3 ((()))
after closed 3 2 ((())
after closed 3 1 ((()
after open 3 0 (((
before closed 2 1 (()
before open 3 1 (()(
before closed 3 2 (()()
before closed 3 3 (()())
after closed 3 3 (()())
after closed 3 2 (()()
after open 3 1 (()(
before closed 2 2 (())
before open 3 2 (())(
before closed 3 3 (())()
after closed 3 3 (())()
after open 3 2 (())(
after closed 2 2 (())
after closed 2 1 (()
after open 2 0 ((
before closed 1 1 ()
before open 2 1 ()(
before open 3 1 ()((
before closed 3 2 ()(()
before closed 3 3 ()(())
after closed 3 3 ()(())
after closed 3 2 ()(()
after open 3 1 ()((
before closed 2 2 ()()
before open 3 2 ()()(
before closed 3 3 ()()()
after closed 3 3 ()()()
after open 3 2 ()()(
after closed 2 2 ()()
after open 2 1 ()(
after closed 1 1 ()
after open 1 0 (
['((()))', '(()())', '(())()', '()(())', '()()()']
"""