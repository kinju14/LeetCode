class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        print(nums)
        i, j = 0, 1
        while i < len(nums):
            if nums[i] != 0:
                i += 1
                j += 1
                continue
            
            while j < len(nums):
                if nums[j] == 0:
                    j += 1 
                    continue
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
                break
            i += 1

        return nums
