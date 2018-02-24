class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        S = []
        for c in A:
            S.append(c)
        rev = []
        while (len(S) > 0):
            rev.append(S.pop())
        return ''.join(rev)


string="abcfoo"

print(string[::-1])
print(string[-1::-1])
print(''.join(reversed(string)))
