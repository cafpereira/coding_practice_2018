# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        prev = None
        cur = A
        i = 1

        # Move cur to starting position
        while cur and i < B:
            prev = cur
            cur = cur.next
            i = i + 1

        # return if no nodes to be reversed at position B
        if not cur:
            return A

        # list can be partitioned into 3 segments: low, mid and hi
        last_low = prev
        first_mid = cur

        # reverse mid segment
        last_mid = self.reverse(first_mid, C - B)

        # if low segment is empty, then the new head is the
        # last node from the mid segment (before reverse)
        if not last_low:
            return last_mid

        # otherwise connect new mid segment with low
        last_low.next = last_mid

        return A

    def reverse(self, head, count):
        prev = head
        ahead = head.next
        j = 0

        # Move forward and reverse pointers
        while ahead and j < count:
            tmp = ahead.next
            ahead.next = prev
            prev = ahead
            ahead = tmp
            j = j + 1

        # Connect last node (reversed) with
        # the remainder of the list
        head.next = ahead

        return prev
