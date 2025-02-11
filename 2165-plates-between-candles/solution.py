class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        result = []

        pipeLeft = [0] * len(s)
        pipeRight = [0] * len(s)
        preItems = [0] * len(s)
        itemsSum = 0
        pipe = -1
        for i in range(len(s)):
            if s[i] == '|':
                pipe = i
            else:
                itemsSum += 1
            preItems[i] = itemsSum
            pipeLeft[i] = pipe

        pipe = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == '|':
                pipe = i
            pipeRight[i] = pipe
        
        # print(pipeRight)
        # print(pipeLeft)

        for [start, end] in queries:
            leftIndx = pipeRight[start]
            rightIndx = pipeLeft[end]

            if leftIndx != -1 and rightIndx != -1 and leftIndx < rightIndx:
                result.append(preItems[rightIndx] - preItems[leftIndx])
            else:
                result.append(0)
        return result
