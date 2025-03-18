class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = str(n)
        product = 1
        sum = 0
        for i in digits:
            sum += int(i)
            product *= int(i)
        return (product - sum)
