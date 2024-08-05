from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l = Counter(arr)

        for s in arr:
            if l[s] == 1:
                k -= 1
                if k == 0:
                    return s
    
        return ""
