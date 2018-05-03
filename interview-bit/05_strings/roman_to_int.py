class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        V = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        last = 0
        for c in reversed(A):
            d = V[c]
            if d < last:
                sum -= d
            else:
                last = d
                sum += d
        return sum


s = Solution()
print(s.romanToInt("XIX"))
