from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = dict(Counter(nums))
        d = dict(sorted(d.items(), key = lambda x: (x[1], -x[0])))
        result = []
        for k, v in d.items():
            result += [k] * v
        return result
