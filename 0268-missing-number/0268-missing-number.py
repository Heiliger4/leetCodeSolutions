class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        oSum, eSum = 0 , 0
        for i in nums:
            oSum += i
        for i in range(len(nums)+1):
            eSum += i
        return eSum - oSum