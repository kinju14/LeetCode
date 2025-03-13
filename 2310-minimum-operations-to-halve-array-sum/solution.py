class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # if len(nums) == 1: return 1
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] *= -1
        target = total / 2
        heapq.heapify(nums)
        k = 0

        while True:
            n = (heapq.heappop(nums)) / 2
            total += n
            k += 1
            if total <= target:
                return k
            heapq.heappush(nums, n)
