class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        minContro = 0
        n = len(arr)
        for i in range(n+1):
            while stack and (i == n or arr[i] < arr[stack[-1]]):
                j = stack.pop()
                left = stack[-1] if stack else -1
                minContro += arr[j] * (j - left) * (i - j)

            stack.append(i)

        return minContro % (10 ** 9 + 7)
