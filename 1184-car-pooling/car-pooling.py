class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        buckets = [0] * 1001

        for people,start,end in trips:
            buckets[start] +=  people
            buckets[end] -=  people

        total = 0
        for people in buckets:
            total += people
            if total > capacity:
                return False
        return True
            