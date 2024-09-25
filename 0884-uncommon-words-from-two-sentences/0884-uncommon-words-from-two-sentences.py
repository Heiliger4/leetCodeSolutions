from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Split the sentences into words
        words1 = s1.split()
        words2 = s2.split()
        
        # Count occurrences of each word in both sentences
        word_count = Counter(words1) + Counter(words2)
        
        # Return words that appear exactly once
        return [word for word, count in word_count.items() if count == 1]

# Example usage:
solution = Solution()
print(solution.uncommonFromSentences("this apple is sweet", "this apple is sour"))  # Output: ['sweet', 'sour']
print(solution.uncommonFromSentences("apple apple", "banana"))  # Output: ['banana']
