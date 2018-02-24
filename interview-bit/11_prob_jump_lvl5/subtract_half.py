# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def makeLinkList(L):
    prev = None
    for v in L:
        node = ListNode(v)
        if prev:
            prev.next = node
        else:
            head = node
        prev = node
    return head


def toArray(L):
    A = []
    while L:
        A.append(L.val)
        L = L.next
    return A


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        n = self.count(A)
        mid = A
        steps = 0
        while steps < n // 2:
            mid = mid.next
            steps += 1

        h1 = A
        h2 = self.reverseList(mid)
        tmp = h2
        prev_mid = None
        while h1 and h2 and (h1 != h2):
            prev_mid = h1
            h1.val = h2.val - h1.val
            h1 = h1.next
            h2 = h2.next

        mid = self.reverseList(tmp)
        if prev_mid:
            prev_mid.next = mid

        return A

    def count(self, L):
        count = 0
        while L:
            count += 1
            L = L.next
        return count

    def reverseList(self, A):
        prev = None
        cur = A
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


# A = makeLinkList([1, 2, 3, 4, 5])
A = makeLinkList([1])

s = Solution()
B = s.subtract(A)
print(toArray(B))
