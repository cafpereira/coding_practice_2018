class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        count = 0

        for v in A:
            if count == 0:
                major = v
                count += 1
            else:
                if v == major:
                    count += 1
                else:
                    count -= 1

        return major
