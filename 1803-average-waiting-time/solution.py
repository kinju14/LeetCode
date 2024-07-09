class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start, finish = customers[0][0], (customers[0][1]+customers[0][0])
        sum = finish - start
        for i in customers[1:]:
            start = finish
            if finish < i[0]: start = i[0]
            finish = start + i[1]
            sum += (finish - i[0])
        return sum/len(customers)
