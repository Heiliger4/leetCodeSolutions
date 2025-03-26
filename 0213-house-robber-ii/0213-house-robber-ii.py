class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(nums):
            prev2, prev1 = 0, nums[0]
            for i in range(1, len(nums)):
                current = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, current
            return prev1
        
        return max(rob_line(nums[1:]), rob_line(nums[:-1]))
