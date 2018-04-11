class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A < 2:
            return A

        min = 0
        max = A
        while min <= max:
            root = (min + max) // 2
            square = root * root
            if square == A:
                return root
            elif square > A:
                max = root - 1
            else:
                min = root + 1

        return max

s = Solution()
print(s.sqrt(2147483647))