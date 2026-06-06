import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush_max(pq,(a,'a'))
        if b > 0:
            heapq.heappush_max(pq,(b,'b'))
        if c > 0:
            heapq.heappush_max(pq,(c,'c'))

        res = ''
        while pq:
            cnt,char = heapq.heappop_max(pq)
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not pq:
                    break
                cnt2,char2 = heapq.heappop_max(pq)
                res += char2
                cnt2 -= 1
                if cnt2 > 0:
                    heapq.heappush_max(pq,(cnt2,char2))
                heapq.heappush_max(pq,(cnt,char))
            else:
                res += char
                cnt -= 1
                if cnt > 0:
                    heapq.heappush_max(pq,(cnt,char))

        return res
            


