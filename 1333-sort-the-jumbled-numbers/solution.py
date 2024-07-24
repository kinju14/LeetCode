class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for n in nums:
            s = int(''.join(list(map(lambda x: str(mapping[int(x)]), str(n)))))
            d[s].append(n)
        d = sorted(d.items(), key = lambda x: x[0])

        result = []
        for v in d:
            result += v[1]
            
        return result
            
