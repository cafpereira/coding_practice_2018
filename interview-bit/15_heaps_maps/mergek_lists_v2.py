from list_node import *

from queue import PriorityQueue


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        heap = PriorityQueue()
        head = None
        prev = None

        for firstNode in A:
            heap.put((firstNode.val, firstNode))

        while not heap.empty():
            min = heap.get()[1]
            cur = ListNode(min.val)

            if min.next:
                next = min.next
                heap.put((next.val, next))

            if not prev:
                head = cur
                prev = cur
            else:
                prev.next = cur
                prev = cur

        return head


A = makeLinkList([1, 10, 20])
B = makeLinkList([4, 11, 13])
C = makeLinkList([3, 8, 9])

s = Solution()
M = s.mergeKLists([A, B, C])
print(toArray(M))
