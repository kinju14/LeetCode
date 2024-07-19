class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        i = 0
        n = len(nums)
        d = defaultdict(list)
        result = []

        while i < n:
            m = len(nums[i])
            for x, k in zip(range(i, i+m), range(m)):
                d[x].append(nums[i][k])

            i += 1
        
        for v in d.values():
            for i in v[::-1]:
                result.append(i)

        return result
        
