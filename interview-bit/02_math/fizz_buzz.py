class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        res = []
        for i in range(1, A + 1):
            fibuz = ''
            if i % 3 == 0:
                fibuz += "Fizz"
            if i % 5 == 0:
                fibuz += "Buzz"

            if fibuz:
                res.append(fibuz)
            else:
                res.append(i)

        return res

s =Solution()
print(s.fizzBuzz(15))