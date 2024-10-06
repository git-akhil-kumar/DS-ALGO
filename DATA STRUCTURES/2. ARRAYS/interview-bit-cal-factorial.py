def solve(num):
    if num <= 1 :
        return 0
    if num == 2 :
        return 2

    res      = [0] * 500
    res[0]   = 2
    res_size = 1
    def cal_fact(num) -> int :
        nonlocal res_size
        carry = 0
        for mul in range(3, num + 1):
            for dig in range(res_size):
                after_mul = (res[dig] * mul) + carry
                res[dig] = after_mul % 10
                carry = after_mul // 10

            while carry :
                res[res_size] = carry % 10
                carry = carry // 10
                res_size += 1

        return res_size
    
    res_size = cal_fact(num)
    res_str = ""

    while res_size >= 0 :
        res_str += str(res[res_size])
        res_size   -= 1

    return res_str


print(solve(2))

print(solve(3))
print(solve(4))
print(solve(5))
print(solve(6))
print(solve(10))
print(solve(15))
print(solve(20))