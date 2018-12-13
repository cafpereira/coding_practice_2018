class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        i, j = 0, 1
        while j < len(A):
            diff = A[j] - A[i]
            if diff == B:
                return 1
            elif diff < B:
                j = j + 1
            else:  # diff > B
                i = i + 1
            if i == j:
                j = i + 1

        return 0

    # https://www.geeksforgeeks.org/find-a-pair-with-the-given-difference
    # This implementation will look the diff for both (i, j) and (j, i) pairs
    def diffPossibleV2(self, A, B):
        size = len(A)

        # Initialize positions of two elements
        i, j = 0, 1

        # Search for a pair
        while i < size and j < size:
            if i != j and A[j] - A[i] == B:
                return 1
            elif A[j] - A[i] < B:
                j += 1
            else:
                i += 1
        return 0

s = Solution()
print(s.diffPossible([1, 5, 7, 9, 10], -2))
print(s.diffPossibleV2([1, 5, 7, 9, 10], -2))
