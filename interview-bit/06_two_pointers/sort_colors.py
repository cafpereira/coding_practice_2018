class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        colors = [0, 0, 0]
        for i in range(len(A)):
            colors[A[i]] += 1

        S = []
        for color, count in enumerate(colors):
            S.extend([color] * count)

        return S


s = Solution()
print(s.sortColors([0, 1, 2, 0, 1, 2]))
