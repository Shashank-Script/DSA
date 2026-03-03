class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = []
        for arr in meetings:
            if not res or arr[0] > res[-1][1]:
                res.append(arr)
            else:
                res[-1][0] = min(arr[0],res[-1][0])
                res[-1][1] = max(arr[1],res[-1][1])

        gap = 0
        for i in range(len(res)):
            if i+1 < len(res):
                gap += res[i+1][0] - res[i][1] - 1

        gap += res[0][0] - 1 # calculation of gaps between day 1 and starting day of meetings(Handling free days before the first meeting)
        gap += days - res[-1][1] # calculation of gaps between final meeting day and remaining days(Handling free days after the last meeting)

        return gap
        
        
