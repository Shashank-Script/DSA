from sortedcontainers import SortedSet
class SummaryRanges:

    def __init__(self):
        self.range = SortedSet()

    def addNum(self, value: int) -> None:
        self.range.add(value)

    def getIntervals(self) -> List[List[int]]:
        if len(self.range) == 0:
            return []

        interval = []
        l = r = None
        for num in self.range:
            if l is None and r is None:
                l = r = num
            elif num == r + 1:
                r = num
            else:
                interval.append([l,r])
                l = r = num
    
        interval.append([l,r])
        return interval

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()