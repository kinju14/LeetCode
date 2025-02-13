import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0 
        while nums[0] < k:
            n1 = heapq.heappop(nums)
            n2 = heapq.heappop(nums)
            heapq.heappush(nums, n1*2 + n2)
            count += 1
        return count
