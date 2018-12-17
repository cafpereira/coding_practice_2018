import re


class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        operands = []
        for token in A:
            if re.search(r'-?\d+', token):  # match number
                operands.append(token)
            else:  # match operator
                op2 = operands.pop()
                op1 = operands.pop()
                res = eval(op1 + token + op2)
                operands.append(str(int(res)))

        return operands.pop()
