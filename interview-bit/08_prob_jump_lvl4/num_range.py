class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        count = 0
        for i in range(len(A)):
            sum = 0
            for j in range(i, len(A)):
                sum += A[j]
                if B <= sum <= C:
                    count += 1
                elif sum > C:
                    break
        return count


s = Solution()
print(s.numRange([10, 5, 1, 0, 2], 6, 8))
