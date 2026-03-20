class SummaryRanges:

    def __init__(self):
        self.range = []

    def addNum(self, value: int) -> None:
        if value not in self.range:
            self.range.append(value)
            self.range.sort()

    def getIntervals(self) -> List[List[int]]:
        if len(self.range) == 0:
            return []

        interval = []
        l = r = None
        for i in range(len(self.range)):
            if l is None and r is None:
                l = r = self.range[i]
            elif self.range[i] == r + 1:
                r = self.range[i]
            else:
                interval.append([l,r])
                l = r = self.range[i]
    
        interval.append([l,r])
        return interval

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()