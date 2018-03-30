class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A = sorted(A)
        n = len(A)
        for i in range(0, n, 2):
            if i + 1 < n:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp

        return A

s = Solution()
print(s.wave([ 11, 8, 7, 9, 2, 10, 2 ]))