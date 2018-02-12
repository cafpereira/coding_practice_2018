import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        if A < 2:
            return [1]
        res = []
        sqrt = int(math.sqrt(A))
        for i in range(1, sqrt + 1):
            if A % i == 0:
                res.append(i)
                cofactor = A // i
                if i != cofactor:
                    res.append(cofactor)

        return sorted(res)
