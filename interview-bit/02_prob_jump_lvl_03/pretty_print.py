class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        d = (2 * A) - 1
        M = [[0 for x in range(d)] for x in range(d)]

        count = A
        while (count > 0):
            offset = A - count
            start = 0 + offset
            end = d - offset
            self.printLayer(M, count, start, end)
            count -= 1
        return M

    def printLayer(self, M, num, start, end):
        for i in range(start, end):
            M[start][i] = num
            M[end - 1][i] = num
            M[i][start] = num
            M[i][end - 1] = num

s = Solution()
print(s.prettyPrint(4))
