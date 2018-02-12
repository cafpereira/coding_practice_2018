def plusOne(A):
    n = len(A)
    start = 0
    for i in range(0, n):
        if A[i] > 0:
            start = i
            break

    carry = 1
    res = []
    for i in range(n - 1, start - 1, -1):
        sum_carry = A[i] + carry
        res.append(sum_carry % 10)
        carry = sum_carry // 10

    if (carry > 0):
        res.append(carry)

    res.reverse()
    return res


A = [1, 2, 7]
print(plusOne(A))
