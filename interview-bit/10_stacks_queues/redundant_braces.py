import re


class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):

        # Track expressions stack
        stack = []

        for c in A:
            if c == '(':
                # start new expression
                stack.append([])
            elif c == ')':
                expr = stack.pop()
                # if closed brace has empty expression (no operators)
                # then return redundant brace
                if not expr:
                    return 1
            else:
                # if no brace seen yet, skip to next sign
                if not stack:
                    continue
                # assume input is valid, there is no need
                # to track operands, just the operators
                if c in '+*-/':
                    stack[-1].append(c)

        # no redundant braces
        return 0
