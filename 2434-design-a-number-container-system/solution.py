class NumberContainers:

    def __init__(self):
        self.indexList = defaultdict(SortedSet)     # 10: [2, 3, 5], 20: [1]
        self.indexToNum = defaultdict()   # 2: 10, 1:10, 3: 10, 5: 10

    def change(self, index: int, number: int) -> None:
        if index in self.indexToNum:
            prev_num = self.indexToNum[index] 
            self.indexList[prev_num].remove(index)
            if len(self.indexList[prev_num]) == 0: del self.indexList[prev_num]


        self.indexList[number].add(index)
        self.indexToNum[index] = number

    def find(self, number: int) -> int:
        if number in self.indexList: return self.indexList[number][0] 
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
