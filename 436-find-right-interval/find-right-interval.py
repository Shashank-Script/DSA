class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        res = n * [0]

        for i in range(n):
            intervals[i].append(i)

        intervals.sort(key=lambda x : x[0])

        for i in range(n):
            l,r = i,n-1
            idx = -1
            while l <= r:
                mid = (l+r)//2
                if intervals[mid][0] >= intervals[i][1]:
                    idx = intervals[mid][2]
                    r = mid - 1
                else:
                    l = mid + 1

            res[intervals[i][2]] = idx
        return res
