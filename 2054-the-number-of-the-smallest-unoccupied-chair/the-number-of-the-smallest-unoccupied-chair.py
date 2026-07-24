class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i in range(len(times)):
            times[i].append(i)

        times.sort(key = lambda x : x[0])
        chairs = []
        record = {}
        for arrive,leave,fri in times:
            for i in range(len(chairs)):
                if chairs[i] <= arrive:
                    chairs[i] = leave
                    record[fri] = i
                    break
            else:
                chairs.append(leave)
                record[fri] = len(chairs)-1

        return record[targetFriend]

            