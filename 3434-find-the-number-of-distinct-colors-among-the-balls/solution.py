class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = []
        b,c = defaultdict(int), defaultdict(int)
        count = 0
        for x, y in queries:
            if x in b:
                prev_c = b[x]
                c[prev_c] -= 1
                if c[prev_c] == 0:
                    del c[prev_c]
                    count -= 1
                if y not in c:
                    count += 1
            else:
                count += 1
                if y in c:
                    count -= 1

            b[x] = y
            c[y] += 1
            result.append(count)
        
        return result
