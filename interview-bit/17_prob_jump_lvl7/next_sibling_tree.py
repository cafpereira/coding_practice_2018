# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

from collections import deque

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        level = deque([])
        level.append(root)

        while level:
            next_level = deque([])
            prev = None
            for node in level:
                if not node:
                    continue
                if prev:
                    prev.next = node
                next_level.append(node.left)
                next_level.append(node.right)
                prev = node
            level = next_level

A = TreeLinkNode(1)
B = TreeLinkNode(2)
C = TreeLinkNode(3)

A.left = B
A.right = C

s = Solution()
s.connect(A)
print(A)
