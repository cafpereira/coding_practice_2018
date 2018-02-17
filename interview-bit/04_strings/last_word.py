class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        W = A.strip().split(" ")
        return len(W[-1])

s = Solution()
print(s.lengthOfLastWord("Hello World   "))
