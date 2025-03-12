class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        print(boxTypes)
        res = 0

        for box, units in boxTypes:
            if box > truckSize:
                res += (truckSize * units) 
                truckSize = 0
            else:
                res += (box * units)
                truckSize -= box

            if truckSize == 0:
                return res
                
        return res
