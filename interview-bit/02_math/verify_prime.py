import math


class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        sqrt = int(math.sqrt(A))

        if A < 2:
            return False

        for i in range(2, sqrt + 1):
            if A % i == 0:
                return 0

        return 1


s = Solution()
print(s.isPrime(84923))
