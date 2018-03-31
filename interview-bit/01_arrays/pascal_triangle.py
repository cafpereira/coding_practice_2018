class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        triangle = []

        for i in range(A):
            prev = 0
            line = []
            if len(triangle) > 0:
                for v in triangle[-1]:
                    next = prev + v
                    line.append(next)
                    prev = v
            line.append(1)
            triangle.append(line)

        return triangle


s = Solution()
print(s.generate(0))
