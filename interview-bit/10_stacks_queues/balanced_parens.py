class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        S = []
        parens = {'(': ')', '[': ']', '{': '}'}
        for c in A:
            if c in parens.values():
                if len(S) == 0:
                    return 0
                top = S.pop()
                if c != parens[top]:
                    return 0
            else:
                S.append(c)

        if len(S) == 0:
            return 1
        else:
            return 0

s = Solution()
print(s.isValid('()[]{}'))
print(s.isValid('([)]'))