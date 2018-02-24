# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        l1 = self.count(A)
        l2 = self.count(B)

        if (l1 < l2):
            tmp = A
            A = B
            B = tmp

        diff = abs(l1 - l2)

        p1 = A
        while diff > 0:
            p1 = p1.next
            diff -= 1

        p2 = B
        while (p1 != None and p2 != None):
            if (p1 == p2):
                return p1
            p1 = p1.next
            p2 = p2.next

        return None

    def count(self, L):
        count = 0
        while L != None:
            count += 1
            L = L.next
        return count
