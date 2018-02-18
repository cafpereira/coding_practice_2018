class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        k = 0
        for i in range(1, len(A)):
            if A[k] != A[i]:
                A[k + 1] = A[i]
                k += 1

        return k + 1


s = Solution()
A = [1, 3, 3, 5]
print(s.removeDuplicates(A))
print(A)