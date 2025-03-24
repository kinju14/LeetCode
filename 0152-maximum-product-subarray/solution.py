class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            temp = currMax
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(temp*n, n*currMin, n)
            res = max(res, currMax)
        return res
                    
        '''
        res = float('-inf')

        for i in range(len(nums)):
            curr = nums[i]
            res = max(res, curr)
            for j in range(i+1, len(nums)):
                curr *= nums[j]
                res = max(res, curr)

        return res     
        '''   
