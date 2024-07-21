class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for _ in range(k)] for _ in range(k)]
        rowIn = [0 for _ in range(k)]
        colIn = [0 for _ in range(k)]
        rowDict = defaultdict(list)
        colDict = defaultdict(list)

        for [i, j] in rowConditions:
            rowIn[j-1] += 1
            rowDict[i].append(j)

        for [i, j] in colConditions:
            colIn[j-1] += 1
            colDict[i].append(j)

        if 0 not in rowIn or 0 not in colIn:
            return []

        row, col = [], []
        while 0 in rowIn:
            idx0 = rowIn.index(0)
            row.append(idx0 + 1)
            rowIn[idx0] = -1
            for i in rowDict[idx0 + 1]:
                rowIn[i-1] -= 1
        if max(rowIn) != -1: return []

        while 0 in colIn:
            idx0 = colIn.index(0)
            col.append(idx0 + 1)
            colIn[idx0] = -1
            for i in colDict[idx0 + 1]:
                colIn[i-1] -= 1
        if max(colIn) != -1: return []

        for i in range(1, k+1):
            r, c = row.index(i), col.index(i)
            matrix[r][c] = i
        
        return matrix
            


        

















        # colIn = defaultdict(lambda: {'indegree': 0, 'next': None})
        # rowIn = defaultdict(lambda: {'indegree': 0, 'next': None})
        
        # colIn, rowIn = {}, {}

        # for [i, j] in rowConditions:
        #     if i in rowIn:
        #         rowIn[i]['indegree'] += 1
        #         rowIn[i]['next'] = j
        #     else:
        #         rowIn[i] = {'indegree': 0, 'next': j}
            
        #     if j in rowIn:
        #         rowIn[j]['indegree'] += 1

        #     else:
        #         rowIn[j] = {'indegree': 0, 'next': None}

        # print(rowIn)


