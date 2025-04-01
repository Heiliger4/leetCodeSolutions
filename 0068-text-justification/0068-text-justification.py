class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, current, num_of_letters = [], [], 0
        
        for word in words:
            if num_of_letters + len(word) + len(current) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    current[i % (len(current) - 1 or 1)] += ' '
                res.append(''.join(current))
                current, num_of_letters = [], 0
            current.append(word)
            num_of_letters += len(word)
        
        return res + [' '.join(current).ljust(maxWidth)]
