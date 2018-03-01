class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        S = set()
        for i in A:
            j1 = i + B
            j2 = i - B
            if j1 in S or j2 in S:
                return 1
            S.add(i)
        return 0
