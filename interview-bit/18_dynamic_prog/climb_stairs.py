class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        stairs = [0] * (A + 2)
        stairs[1] = 1
        for i in range(A):
            cur = i + 2
            stairs[cur] = stairs[cur - 1] + stairs[cur - 2]

        return stairs[-1]

s = Solution()
print(s.climbStairs(3))
