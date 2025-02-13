class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        result = 0
        while i<j:
            result = max(result, min(height[i], height[j]) * (j-i))
            # print(result)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result

