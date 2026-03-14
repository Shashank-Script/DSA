from sortedcontainers import SortedDict
class MyCalendar:

    def __init__(self):
        self.booked = SortedDict()
        

    def book(self, startTime: int, endTime: int) -> bool:
        self.booked[startTime] = self.booked.get(startTime,0) + 1
        self.booked[endTime] = self.booked.get(endTime,0) - 1

        overlap = 0
        for val in self.booked.values():
            overlap += val
            if overlap > 1:
                self.booked[startTime] = self.booked.get(startTime,0) - 1
                if self.booked[startTime] == 0:
                    del self.booked[startTime]
                self.booked[endTime] = self.booked.get(endTime,0) + 1
                if self.booked[endTime] == 0:
                    del self.booked[endTime]
                return False
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)