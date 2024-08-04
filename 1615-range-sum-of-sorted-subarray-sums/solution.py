class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l = []
        for i in range(n):
            total = nums[i]
            l.append(total)
            for j in range(i+1, n):
                total += nums[j]
                l.append(total)
        l.sort()
        return sum(l[left-1:right]) % (10**9 + 7)


