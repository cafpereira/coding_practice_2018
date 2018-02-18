class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        i, j = len(A) - 1, len(A) - 1
        while i >= 0:
            if i == j:
                i -= 1
                continue

            sub = A[j] - A[i]

            if sub == B:
                return 1
            elif sub > B:
                j -= 1
            else:  # sub < B
                i -= 1
        return 0

s = Solution()
print(s.diffPossible([1, 3, 7, 12], 2))
