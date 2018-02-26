class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if B == 0:
            return 1 % C
        n2 = self.Mod(A, B // 2, C) % C

        power = n2 * n2
        if B % 2 == 1:
            power = power * (A % C)

        return power % C


s = Solution()
print(s.Mod(5, 2, 7))
print(s.Mod(5, 3, 7))
