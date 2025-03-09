class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res = 0

        for l in range(len(colors)):
            r = (l+2) % len(colors)
            if colors[l] == colors[r] and colors[(l+1)%len(colors)] != colors[l]:
                res += 1
        
        return res
