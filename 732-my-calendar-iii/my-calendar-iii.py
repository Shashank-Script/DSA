from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.calendar = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.calendar[startTime] = self.calendar.get(startTime,0) + 1
        self.calendar[endTime] = self.calendar.get(endTime,0) - 1

        maxx = 0
        booking = 0

        for val in self.calendar.values():
            booking += val
            if booking > maxx:
                maxx = booking
        return maxx


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)