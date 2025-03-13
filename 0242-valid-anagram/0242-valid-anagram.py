class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tmp_list = list(t)
        for i in s:
            if i in tmp_list:
                tmp_list.remove(i)
            else:
                return False

        return len(tmp_list) == 0
            
