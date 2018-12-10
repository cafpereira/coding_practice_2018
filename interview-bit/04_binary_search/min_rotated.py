class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        start = 0
        end = len(A) - 1

        while start < end:
            mid = (start + end) // 2
            if A[mid] > A[end]:
                # Min must be in range [mid+1,end]
                start = mid + 1
            else: # A[mid] < A[end]
                # Min must be in range [start,mid]
                end = mid

        return A[start]


s = Solution()
print(s.findMin([4, 5, 6, 7, 1, 2, 3]))
