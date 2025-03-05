class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        evenPos = (n + 1) // 2
        oddPos = n // 2
        combination = (pow(5, evenPos, MOD) * pow(4, oddPos, MOD)) % MOD
        return combination