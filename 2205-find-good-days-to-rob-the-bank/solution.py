class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return [n for n in range(len(security))]

        elif len(security) < time * 2 + 1:
            return []

        nonIncreasing = [0] * len(security)
        nonDecreasing = [0] * len(security)

        for i in range(1, len(security)):
            if security[i] <= security[i-1]:
                nonIncreasing[i] = nonIncreasing[i-1] + 1

        
        for i in range(len(security)-2, -1, -1):
            if security[i] <= security[i+1]:
                nonDecreasing[i] = nonDecreasing[i+1] + 1
            
        res = []
        for i in range(len(security)):
            if nonIncreasing[i] >= time and nonDecreasing[i] >= time:
                res.append(i)

        return res
        
