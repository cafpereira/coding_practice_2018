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
