class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        l, r = 0, 0
        while r < k:
            if blocks[r] == 'W':
                whites += 1
            r += 1
        res = whites

        while r < len(blocks):
            if blocks[r] == 'W':
                whites += 1
            if blocks[l] == 'W':
                whites -= 1
            res = min(res, whites)
            r += 1
            l += 1
        return res
