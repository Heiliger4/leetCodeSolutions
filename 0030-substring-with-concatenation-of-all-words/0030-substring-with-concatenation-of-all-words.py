class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        word_map = {}
        result = []
        
        # count frequency of each word in words
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        
        for i in range(word_len):
            left = i
            right = i
            current_map = {}
            count = 0
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_map:
                    current_map[word] = current_map.get(word, 0) + 1
                    count += 1
                    
                    # if too many of word, move left pointer
                    while current_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        current_map[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # if found valid substring
                    if count == word_count:
                        result.append(left)
                else:
                    current_map.clear()
                    count = 0
                    left = right
        
        return result
