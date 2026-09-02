class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x : x[0])
        meeting_count = {}
        rooms = list(range(n))
        heapq.heapify(rooms)
        occupied = []


        for start,end in meetings:
            while occupied:
                freeAt,room = occupied[0]
                if start >= freeAt:
                    end_time,free_room = heapq.heappop(occupied)
                    heapq.heappush(rooms,free_room)
                else:break

            if rooms:
                room = heapq.heappop(rooms)
                heapq.heappush(occupied,(end,room))
                meeting_count[room] = meeting_count.get(room,0) + 1
            else:
                end_time,free_room = heapq.heappop(occupied)
                diff = end - start
                heapq.heappush(occupied,(end_time + diff,free_room))
                meeting_count[free_room] = meeting_count.get(free_room,0) + 1
        
        ans = max(meeting_count, key=lambda k: (meeting_count[k], -k))
        return ans


