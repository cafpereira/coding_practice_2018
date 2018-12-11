class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        p = 0
        exit = False
        while not exit:
            cur = None
            for stri in A:
                if p >= len(stri):
                    exit = True
                    break
                if not cur:
                    cur = stri[p]
                else:
                    if stri[p] != cur:
                        exit = True
                        break
            if not exit:
                p = p + 1

        first = A[0]
        return first[:p]


s = Solution()

A = ['abcdefgh',
     'aefghijk',
     'abcefgh']

print(s.longestCommonPrefix(A))
