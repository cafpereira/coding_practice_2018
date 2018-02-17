class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        L = []
        L.extend(A)
        L = self.reverse(L, 0, len(L) - 1)

        start = self.advance(L, 0)
        end = self.advance(L, start + 1, space=True)
        while end < len(L):
            self.reverse(L, start, end)
            start = self.advance(L, end + 1)
            end = self.advance(L, start + 1, space=True)
        if start < end:
            self.reverse(L, start, end - 1)
        return ''.join(L)

    def reverse(self, L, start, end):
        while start < end:
            tmp = L[start]
            L[start] = L[end]
            L[end] = tmp
            start += 1
            end -= 1
        return L

    def advance(self, L, i, space=False):
        while i < len(L):
            if not space:
                if L[i] != ' ':
                    break
            else:
                if L[i] == ' ':
                    return i - 1
            i += 1
        return i


s = Solution()
print(s.reverseWords("the sky is blue"))
