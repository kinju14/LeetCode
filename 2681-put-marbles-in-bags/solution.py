class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        pairSums = [weights[i]+weights[i+1] for i in range(len(weights)-1)]
        pairSums.sort()

        minScore = sum(pairSums[:k-1])
        maxScore = sum(pairSums[-(k-1):])
        return maxScore - minScore

