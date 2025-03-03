class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # check each number to the rest of the array if it can make the target #no
        # if so find the index of both elements
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]