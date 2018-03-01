class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        res = []
        perm = []
        count = self.countVals(A)
        self.permuteCount(count, perm, res, len(A))
        return res

    def permuteCount(self, count, perm, res, n):
        if len(perm) == n:
            res.append(perm[:])
            return

        for (k, v) in count.items():
            if v > 0:
                count[k] -= 1
                perm.append(k)
                self.permuteCount(count, perm, res, n)
                perm.pop()
                count[k] += 1

    def countVals(self, A):
        count = {}
        for x in A:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        return count


s = Solution()
print(s.permute([1, 1, 2]))
