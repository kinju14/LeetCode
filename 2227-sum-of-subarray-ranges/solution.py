class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        
        def largest():
            stack = []
            maxContro = 0
            for i in range(n+1):
                while stack and (i == n or nums[i] > nums[stack[-1]]):
                    j = stack.pop()
                    left = stack[-1] if stack else -1
                    maxContro += nums[j] * (j - left) * (i - j)

                stack.append(i)
            return maxContro

        
        def smallest():
            stack = []
            minContro = 0
            for i in range(n+1):
                while stack and (i == n or nums[i] < nums[stack[-1]]):
                    j = stack.pop()
                    left = stack[-1] if stack else -1
                    minContro += nums[j] * (j - left) * (i - j)

                stack.append(i)
            return minContro

        return largest() - smallest()
