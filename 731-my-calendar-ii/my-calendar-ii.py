class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.booked2 = []


    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.booked) == 0:
            self.booked.append([startTime, endTime-1])
            return True

        for start,end in self.booked2:
            if startTime <= end and endTime-1 >= start:
                return False
        
        for start,end in self.booked:
            if startTime <= end and endTime-1 >= start:
                self.booked2.append([max(start,startTime),min(end,endTime-1)])
            
        self.booked.append([startTime, endTime-1])
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)