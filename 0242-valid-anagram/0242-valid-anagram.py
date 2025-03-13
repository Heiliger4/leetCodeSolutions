class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)
'''
        #is diff len: early out
        if len(s) != len(t):
            return False
        
        #make a list of the incomming string then iterate over the main string while removing each ele from the list if they appear on the main string
        tmp_list = list(t)
        for i in s:
            if i in tmp_list:
                tmp_list.remove(i)
            else:
                return False
#if all gets removed then ANAGRAM
        return len(tmp_list) == 0
'''

            
