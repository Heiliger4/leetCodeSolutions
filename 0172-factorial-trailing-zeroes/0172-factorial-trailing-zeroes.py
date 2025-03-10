class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Find the factorial of the number and then check how many trailing zeros there are
        # Factorial of 0 or 1 doesn't have trailing zeros
        if n == 0 or n == 1:
            return 0  
        # Calculate the factorial of n (which is very large)
        def factorial(num: int) -> int:
            if num == 0 or num == 1:
                return 1
            return num * factorial(num - 1)

        # Find the factorial of n
        answer = factorial(n)
        
        # Count trailing zeros
        count = 0
        while answer % 10 == 0 and answer !=0:
            answer //= 10
            count += 1
        
        return count
