class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A < 1:
            return []

        triangle = [[1]]
        if A < 2:
            return triangle

        for i in range(A - 1):
            prev = 0
            line = []
            for v in triangle[i]:
                next = prev + v
                line.append(next)
                prev = v
            line.append(1)
            triangle.append(line)

        return triangle


s = Solution()
print(s.generate(5))
