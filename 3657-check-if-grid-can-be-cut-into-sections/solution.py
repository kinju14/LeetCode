class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        start = []
        end = []
        for st_x, st_y, e_x, e_y in rectangles:
            start.append([st_x, e_x])
            end.append([st_y, e_y])
        start.sort(key = lambda x: x[0])
        end.sort(key = lambda x: x[0])
        def canPartition(arr):
            count = 0
            prev_end = -1
            for s, e in arr:
                if prev_end <= s:
                    count += 1
                prev_end = max(prev_end, e)
            return count >= 3

        return canPartition(start) or canPartition(end)

            
