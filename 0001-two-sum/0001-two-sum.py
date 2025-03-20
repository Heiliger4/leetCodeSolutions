class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # check each number to the rest of the array if it can make the target #no
        # if so return index of both elements
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return[i, j]