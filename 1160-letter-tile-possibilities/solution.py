class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = dict(Counter(tiles))
        # perm = []

        def backtrack():
            res = 0
            # if len(perm) == len(tiles):
            #     return 0
            
            for n in count:
                if count[n] > 0:
                    # perm.append(n)
                    res += 1
                    count[n] -= 1

                    res += backtrack()
                    count[n] += 1
                    # perm.pop()

            return res

        return backtrack()

        


        
