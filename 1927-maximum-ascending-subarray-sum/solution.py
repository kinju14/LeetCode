class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        i, sum = 0,0
        temp_sum = nums[i]
        while i<n-1:
            # for j in range(i,n-1):
            if nums[i+1] > nums[i]:
                temp_sum += nums[i+1]
            else: 
                if sum < temp_sum: 
                    sum = temp_sum
                temp_sum = nums[i+1]

            i += 1
            
        
        return max(sum, temp_sum)
