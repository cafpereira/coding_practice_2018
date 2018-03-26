import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        nums = [True] * (A + 1)

        sqr = int(math.sqrt(A))

        for i in range(2, sqr + 1):
            if nums[i]:
                next = 2 * i
                while next <= A:
                    nums[next] = False
                    next += i

        primes = []
        for i in range(2, A + 1):
            if nums[i]:
                primes.append(i)

        return primes


s = Solution()
print(s.sieve(10))
