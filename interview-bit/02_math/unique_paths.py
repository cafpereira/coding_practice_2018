class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        grid = [[0] * B for i in range(A)]

        for i in range(A):
            for j in range(B):
                if i == 0 or j == 0:
                    grid[i][j] = 1
                else:
                    up = grid[i - 1][j]
                    left = grid[i][j - 1]
                    grid[i][j] = up + left

        return grid[A - 1][B - 1]
