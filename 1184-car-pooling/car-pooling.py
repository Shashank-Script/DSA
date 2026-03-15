from sortedcontainers import SortedDict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = SortedDict()
        for people,start,end in trips:
            car[start] = car.get(start,0) + people
            car[end] = car.get(end,0) - people

        total = 0
        for val in car.values():
            total += val
            if total > capacity:
                return False
        return True
            
