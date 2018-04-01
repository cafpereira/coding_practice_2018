class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        start = 0
        end = len(A) - 1

        while end > start:
            mid = (start + end) // 2
            if mid > 0 and A[mid - 1] > A[mid]:
                return A[mid]

            if A[mid] < A[end]:
                end = mid - 1
            else:
                start = mid + 1

        return A[start]


s = Solution()
print(s.findMin([4, 5, 6, 7, 1, 2, 3]))
