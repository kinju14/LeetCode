class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            val = target - nums[i]
            for j in range(i+1, n):
                if nums[j] == val:
                    return [i, j]
                

                
