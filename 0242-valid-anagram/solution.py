from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if set(s) != set(t): return False

        d1, d2 = {}, {}
        for ch in s:
            if ch not in d1:
                d1[ch] = 1
            else:
                d1[ch] += 1

        for ch in t:
            if ch not in d2:
                d2[ch] = 1
            else:
                d2[ch] += 1
    
        for i in d1.keys():
            if i not in d2.keys() or d1[i] != d2[i]: return False

        return True
