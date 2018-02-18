class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        size = len(A) + len(B)
        M = [0] * size

        i, j = len(A) - 1, len(B) - 1
        k = size - 1

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                M[k] = A[i]
                i -= 1
            else:
                M[k] = B[j]
                j -= 1
            k -= 1

        for l in range(i, -1, -1):
            M[k] = A[l]
            k -= 1

        for l in range(j, -1, -1):
            M[k] = B[l]
            k -= 1

        return M


s = Solution()
print(s.merge([1, 3, 3, 5], [3, 3, 5]))
