class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        suc = None
        cur = A
        while cur:
            if cur.val > B:
                suc = cur
                cur = cur.left
            else:
                cur = cur.right

        return suc


s = Solution()
s.getSuccessor(None, 10)
