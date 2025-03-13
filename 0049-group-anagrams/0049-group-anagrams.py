from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ using a dictionary where the key is a tuple representing the frequency count of each letter in a string, and the value is a list of strings that share the same letter frequency (i.e., anagrams). 
        iterate through the input list, 
        calculate the frequency count for each string, and 
        group anagrams together based on this key. 
        return the grouped anagrams."""
        res = defaultdict(list)
        for s in strs:
# Initialize a list of 26 zeros to count occurrences of each letter ('a' to 'z')
            count = [0] * 26  
            for c in s:
                count[ord(c) - ord('a')] += 1  
            res[tuple(count)].append(s)  
        return list(res.values())  
