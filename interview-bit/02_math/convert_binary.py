class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        bin = []

        if A == 0:
            bin.append("0")

        while A:
            bit = A & 1
            bin.append(str(bit))
            A >>= 1

        res = list(reversed(bin))
        return ''.join(res)


s = Solution()
print(s.findDigitsInBinary(17))
