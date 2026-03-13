from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.treemap = SortedDict()
        
    def book(self, startTime: int, endTime: int) -> bool:
        self.treemap[startTime] = self.treemap.get(startTime,0) + 1
        self.treemap[endTime] = self.treemap.get(endTime,0) + -1

        rooms = 0
        for val in self.treemap.values():
            rooms += val
            if rooms > 2:
                self.treemap[startTime] = self.treemap.get(startTime,0) - 1
                self.treemap[endTime] = self.treemap.get(endTime,0) + 1

                if self.treemap[startTime] == 0:
                    del self.treemap[startTime]
                if self.treemap[endTime] == 0:
                    del self.treemap[endTime]

                return False

        return True


        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)