class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        low = B - 0.5
        hi = B + 0.5

        first = self.binSearch(A, low)
        last = self.binSearch(A, hi)

        return last - first

    def binSearch(self, A, val):
        start = 0
        end = len(A) - 1

        while start <= end:
            mid = (start + end) // 2
            if A[mid] > val:
                end = mid - 1
            else:  # A[mid] < val (we know val inputs are not in the array)
                start = mid + 1

        return start

s = Solution()

#    0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7  8  9  0  01  02  03
A = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10]
B = 0
print(s.findCount(A, B))
