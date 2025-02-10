class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        buckets = [[] for _ in range(len(nums))]

        for n in nums:
            d[n] += 1

        for n, c in d.items():
            buckets[c-1].append(n)

        result = []
        for i in range(len(nums)-1, -1, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result
