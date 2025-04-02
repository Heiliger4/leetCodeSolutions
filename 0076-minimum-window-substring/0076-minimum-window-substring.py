class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        s_count = Counter()
        required = len(t_count)
        formed = 0
        left, right = 0, 0
        min_len = float("inf")
        min_window = ""
        
        while right < len(s):
            char = s[right]
            s_count[char] += 1
            
            if char in t_count and s_count[char] == t_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                
                s_count[char] -= 1
                if char in t_count and s_count[char] < t_count[char]:
                    formed -= 1
                left += 1
            
            right += 1
        
        return min_window
