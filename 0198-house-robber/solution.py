class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[-1]
        '''
        Top Down DP
        n = len(nums)
        if n == 1:
                return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        dp = [-1] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        def helper(i):
            if dp[i] != -1:
                return dp[i]
            else:
                dp[i] = max(nums[i]+helper(i-2), helper(i-1))
                return dp[i]

        return helper(n-1)

        DP Space Optimized
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
        '''
