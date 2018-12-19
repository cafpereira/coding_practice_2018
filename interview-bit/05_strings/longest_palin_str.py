class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)
        dp = [[False] * n for i in range(n)]

        start, end = 0, 0
        max_size = 0

        for step in range(n):
            size = step + 1
            for i in range(n - step):
                j = i + step

                if j > i + 1:
                    palin = A[i] == A[j] and dp[i + 1][j - 1]
                else:
                    palin = A[i] == A[j]

                dp[i][j] = palin

                if palin and size > max_size:
                    start, end = i, j + 1
                    max_size = size

        return A[start:end]


s = Solution()
print(s.longestPalindrome('abbcccbbbcaaccbababcbcabca')) ## expect: bbcccbb
