class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):

        for cur in range(len(A)):
            i = cur
            match = True
            for j in range(len(B)):
                match = i < len(A) and A[i] == B[j]
                if not match:
                    break
                else:
                    i += 1
            if match:
                return cur

        return -1


s = Solution()
print(s.strStr("", "oo"))
