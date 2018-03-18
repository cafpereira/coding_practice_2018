# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : integer
    # @return a list of TreeNode
    def generateTrees(self, A):
        values = list(range(1, A + 1))
        return self.generateTreesHelper(values)

    def generateTreesHelper(self, A):
        if not A:
            return [None]

        res = []
        for pivot in A:
            left = [v for v in A if v < pivot]
            leftTrees = self.generateTreesHelper(left)

            right = [v for v in A if v > pivot]
            rightTrees = self.generateTreesHelper(right)

            for leftRoot in leftTrees:
                for rightRoot in rightTrees:
                    root = TreeNode(pivot)
                    root.left = leftRoot
                    root.right = rightRoot
                    res.append(root)
        return res


def postOrderAll(res):
    return [postOrder(tree) for tree in res]


def postOrder(root):
    order = []
    postOrderHelper(root, order)
    return order


def postOrderHelper(root, order):
    if not root:
        return
    postOrderHelper(root.left, order)
    postOrderHelper(root.right, order)
    order.append(root.val)

s = Solution()
res = s.generateTrees(3)
print(postOrderAll(res))
