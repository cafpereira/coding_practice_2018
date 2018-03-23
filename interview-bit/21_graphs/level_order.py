# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        res = []
        q = [A]

        while q:
            values = []
            next_level = []
            for node in q:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                values.append(node.val)
            res.append(values)
            q = next_level

        return res


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)

A.left = B
A.right = C

s = Solution()
print(s.levelOrder(A))
