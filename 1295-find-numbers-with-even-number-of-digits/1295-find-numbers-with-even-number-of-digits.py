# 
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            isEven = len(str(num))
            if isEven % 2 == 0:
                count+=1
        return count