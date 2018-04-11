class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        start = 0
        end = len(A) - 1

        while start <= end:
            mid = (start + end) // 2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1

        return start


s = Solution()
A = [1, 3, 5, 6]

print(s.searchInsert(A, 5))
print(s.searchInsert(A, 2))
print(s.searchInsert(A, 7))
print(s.searchInsert(A, 0))
