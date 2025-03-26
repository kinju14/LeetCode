class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        for row in grid:
            for n in row:
                if n % x != grid[0][0] % x:
                    return -1

        nums = [n for row in grid for n in row]
        nums.sort()
        median = nums[len(nums)//2]
        res = 0
        for n in nums:  
            res += abs(n - median) // x
        return res  
