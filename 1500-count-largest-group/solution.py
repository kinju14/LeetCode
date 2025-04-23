class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sumN(x: int):
            return sum(int(d) for d in str(x))

        hashmap = defaultdict(int)
        for i in range(1, n+1):
            hashmap[sumN(i)] += 1
        
        maxSize = max(hashmap.values())
        return sum(1 for x in hashmap.values() if x == maxSize)
