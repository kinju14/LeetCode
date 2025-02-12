class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = dict()
        for i, num in enumerate(nums):
            n, total = num, 0
            while n > 0:
                total += n % 10
                n //= 10
            if total in d:
                if d[total][0] <= num:
                    d[total][1] = d[total][0]
                    d[total][0] = num
                elif d[total][1] < num:
                    d[total][1] = num
            else: d[total] = [num, -1]
    
        result = -1
        for key in d:
            if d[key][1] != -1:
                result = max(result, d[key][0]+d[key][1])
        return result
