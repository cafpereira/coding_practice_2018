class Solution:
    # @param A : list of integers
    # @return an integer
    def countInversions(self, A):
        n = len(A)
        return self.countInversionsHelper(A, 0, n - 1)

    def countInversionsHelper(self, A, start, end):
        if start >= end:
            return 0

        mid = (start + end) // 2

        left = self.countInversionsHelper(A, start, mid)
        right = self.countInversionsHelper(A, mid + 1, end)
        split = self.merge(A, start, mid, end)

        return left + right + split

    def merge(self, A, start, mid, end):
        M = []
        L = A[start: mid + 1]
        H = A[mid + 1: end + 1]

        split = 0
        while L and H:
            if L[0] <= H[0]:
                M.append(L.pop(0))
            else:
                split += len(L)
                M.append(H.pop(0))

        if L:
            for v in L:
                M.append(v)
        else:
            for v in H:
                M.append(v)

        for i in range(start, end + 1):
            A[i] = M.pop(0)

        return split


s = Solution()
# A = [1 , 2, 1]
A = [2, 4, 1, 3, 5]

print(s.countInversions(A))
print(A)
