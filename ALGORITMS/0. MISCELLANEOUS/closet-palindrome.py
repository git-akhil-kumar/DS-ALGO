# LEETCODE 564 :- https://leetcode.com/problems/find-the-closest-palindrome/description/


def nearestPalindromic(s: str) -> str:
    n = len(s)
    num = int(s)

    if n == 1:
        return str(num - 1)

    nine = pow(10, n - 1) - 1
    onezeros = pow(10, n) + 1

    halflen = (n + 1) // 2
    prefix = int(s[:halflen])
    candidates = set([nine, onezeros])

    for i in [-1, 0, 1]:
        newprefix = str(prefix + i)
        if n % 2 == 0:
            palindrome = int(newprefix + newprefix[::-1])
        else:
            palindrome = int(newprefix + newprefix[-2::-1])
        candidates.add(palindrome)
    candidates.discard(num)
    closest = min(candidates, key=lambda x: (abs(x - num), x))
    return str(closest)


testcases = ["100", "198", "99", "1", "12321", "999"]
for testcase in testcases:
    print("answer for", testcase, "=", nearestPalindromic(testcase))
