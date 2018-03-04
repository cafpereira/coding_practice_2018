from list_node import *

import heapq


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        heap = []
        head = None
        prev = None

        for i, node in enumerate(A):
            heapq.heappush(heap, (node.val, {'idx': i, 'node': node}))

        while len(heap) > 0:
            pop = heapq.heappop(heap)[1]
            min = pop['node']
            cur = ListNode(min.val)

            if min.next:
                nextn = min.next
                heapq.heappush(heap, (nextn.val, {'idx': pop['idx'], 'node': nextn}))

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
