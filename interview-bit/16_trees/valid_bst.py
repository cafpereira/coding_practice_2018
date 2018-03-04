# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        if self.isValidBSTHelper(A, float('-inf'), float('inf')):
            return 1
        else:
            return 0

    def isValidBSTHelper(self, node, min, max):
        if not node:
            return True
        if min < node.val < max:
            return self.isValidBSTHelper(node.left, min, node.val) and \
                   self.isValidBSTHelper(node.right, node.val, max)
        else:
            return False


s = Solution()
s.isValidBST(None)
