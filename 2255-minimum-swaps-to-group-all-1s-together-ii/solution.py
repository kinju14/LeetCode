class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        totalOnes = nums.count(1)
        i, j = 0, 0
        nums = nums+nums
        n = len(nums)
        maxOnes = 0
        while j < totalOnes:
            if nums[j] == 1: maxOnes += 1
            j += 1

        currOnes = maxOnes
        
        while j < n-1:
            if nums[i] == 1:
                currOnes -= 1
            i += 1
            j += 1
            if nums[j-1] == 1:
                currOnes += 1
            maxOnes = max(maxOnes, currOnes)            

        return totalOnes - maxOnes
            

