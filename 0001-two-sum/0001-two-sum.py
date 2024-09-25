class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the indices of the numbers
        hashmap = {}
        
        # Iterate over the list
        for i, num in enumerate(nums):
            complement = target - num
            # Check if the complement exists in the hashmap
            if complement in hashmap:
                return [hashmap[complement], i]  # Return indices of the complement and current number
            # Otherwise, store the current number with its index
            hashmap[num] = i

# Example usage:
# solution = Solution()
# print(solution.twoSum([2,7,11,15], 9))  # Output: [0, 1]
# print(solution.twoSum([3,2,4], 6))  # Output: [1, 2]
# print(solution.twoSum([3,3], 6))  # Output: [0, 1]
