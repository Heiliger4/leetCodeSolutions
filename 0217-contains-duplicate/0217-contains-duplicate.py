class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = len(set(nums))
        original = len(nums)
        if(unique == original):
            return False
        else:
            return True