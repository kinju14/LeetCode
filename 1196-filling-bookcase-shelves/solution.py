class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        result = {}
        n = len(books)
        def recursive(i: int):
            if i == n:
                return 0
            if i in result:
                return result[i]

            currShelfWidth = shelfWidth
            maxHeight = 0
            result[i] = float('inf')
            for j in range(i, n):
                w, h = books[j]
                if currShelfWidth < w: break
                currShelfWidth -= w
                maxHeight = max(maxHeight, h)
                result[i] = min(result[i], recursive(j+1) + maxHeight)

            return result[i]
        return recursive(0)

