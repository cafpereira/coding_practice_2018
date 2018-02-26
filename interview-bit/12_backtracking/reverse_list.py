from list_node import *


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        return self.reverseRec(None, A)

    def reverseRec(self, prev, cur):
        if not cur:
            return prev

        head = self.reverseRec(cur, cur.next)
        cur.next = prev

        return head


# A = makeLinkList([1, 2, 3, 4, 5])
A = makeLinkList([1])

s = Solution()
B = s.reverseList(A)
print(toArray(B))
