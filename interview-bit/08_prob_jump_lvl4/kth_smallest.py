class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        while B <= len(A):
            mid = len(A) // 2
            pivot = A[mid]
            less, equal, greater = [], [], []
            for i in range(len(A)):
                if A[i] < pivot:
                    less.append(A[i])
                elif A[i] > pivot:
                    greater.append(A[i])
                else:
                    equal.append(A[i])
            if len(less) >= B:
                A = less
            elif len(less) < B <= len(less) + len(equal):
                return pivot
            else:
                B = B - (len(less) + len(equal))
                A = greater
        return -1


s = Solution()
# print(s.kthsmallest((2, 1, 4, 3, 2), 3))

A = (
54, 96, 30, 79, 95, 6, 93, 91, 93, 63, 56, 11, 30, 58, 31, 100, 81, 25, 21, 76, 60, 18, 84, 8, 94, 3, 25, 84, 33, 74)
B = 2

print(sorted(A))
print(s.kthsmallest(A, B))
