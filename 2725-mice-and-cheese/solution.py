class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        if k == 0:
            return sum(reward2)

        if k == 1 and len(reward1) == 1:
            return reward1[0]

        score = 0
        n = len(reward1)
        mergedList = []

        for i in range(n):
            mergedList.append([reward1[i], reward2[i]])

        mergedList = sorted(mergedList, key = lambda x: x[0] - x[1])

        for i in range(n-1, -1, -1):
            if k > 0 :
                score += mergedList[i][0]
                k -= 1
            else:
                score += mergedList[i][1]
            
        return score

        
