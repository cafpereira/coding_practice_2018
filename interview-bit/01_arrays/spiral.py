class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        m = len(A)
        n = len(A[0])
        S = []

        first_row = 0
        last_row = m - 1

        first_col = 0
        last_col = n - 1

        while (len(S) < m * n):
            if (first_row <= last_row):
                for j in range(first_col, last_col + 1):
                    S.append(A[first_row][j])
                first_row += 1

            if (first_col <= last_col):
                for i in range(first_row, last_row + 1):
                    S.append(A[i][last_col])
                last_col -= 1

            if (first_row <= last_row):
                for j in range(last_col, first_col - 1, -1):
                    S.append(A[last_row][j])
                last_row -= 1

            if (first_col <= last_col):
                for i in range(last_row, first_row - 1, -1):
                    S.append(A[i][first_col])
                first_col += 1

        return S
