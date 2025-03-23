class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        res = 0
        total = 0

        for i in range(n):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        return res
        
        '''
        def canReach(idx):
            count = n
            tank = gas[idx]

            while count > 0:
                if tank < cost[idx % n]:
                    return False
                tank = tank - cost[idx%n] + gas[(idx+1)%n]
                idx += 1
                count -= 1
            return True

        for i in range(n):
            if gas[i] < cost[i]:
                continue
            else:
                if canReach(i):
                    return i
        return -1
        ''' 
