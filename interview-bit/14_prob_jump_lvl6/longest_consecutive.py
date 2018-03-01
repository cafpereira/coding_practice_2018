class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        S = set()
        res = 0
        for i in A:
            S.add(i)

        for i in A:
            if i + 1 in S:
                continue
            count = 1
            prev = i - 1
            while prev in S:
                count += 1
                prev -= 1
            res = max(res, count)

        return res

s = Solution()
A = [100, 4, 200, 1, 3, 2]
print(s.longestConsecutive(A))