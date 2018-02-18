class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        I = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                i += 1
            elif B[j] < A[i]:
                j += 1
            else:
                I.append(A[i])
                i += 1
                j += 1
        return I

s = Solution()
print(s.intersect([1, 3, 3, 5], [3, 3, 5]))

