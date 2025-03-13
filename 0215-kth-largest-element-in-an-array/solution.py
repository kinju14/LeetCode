class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        print(nums)
        i = 0
        while i < k-1:
            heapq.heappop(nums)
            i += 1 

        return nums[0] * -1

