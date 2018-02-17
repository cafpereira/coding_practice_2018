class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        start = self.advance(A, 0, 1)
        end = self.advance(A, len(A) - 1, -1)

        while start < end:
            if A[start].lower() != A[end].lower():
                return 0
            start = self.advance(A, start + 1, 1)
            end = self.advance(A, end - 1, -1)
        return 1

    def advance(self, A, ptr, inc):
        while 0 <= ptr < len(A):
            if A[ptr].isdigit() or A[ptr].isalpha():
                return ptr
            ptr += inc
        return ptr


s = Solution()

print(s.isPalindrome("R!aB'ar"))
