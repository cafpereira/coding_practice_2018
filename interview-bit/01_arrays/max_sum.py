'''
Max Sum Contiguous Subarray
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxSum = A[0]
        curSum = 0

        for v in A:
            curSum = curSum + v
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0

        return maxSum
