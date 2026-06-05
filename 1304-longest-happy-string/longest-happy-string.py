class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        cnt_a = cnt_b = cnt_c = 0
        while True:
            if a > 0 and ((a >= b and a >= c and cnt_a < 2) or (b >= a >= c and cnt_b == 2) or (c >= a >= b and cnt_c == 2)):
                res += 'a'
                cnt_a += 1
                cnt_b = cnt_c = 0
                a -= 1
            elif b > 0 and ((b >= a and b >= c and cnt_b < 2) or (a >= b >= c and cnt_a == 2) or (c >= b >= a and cnt_c == 2)) :
                res += 'b'
                cnt_b += 1
                cnt_a = cnt_c = 0
                b -= 1
            elif c > 0 and ((c >= a and c >= b and cnt_c < 2) or (a >= c >= b and cnt_a == 2) or (b >= c >= a and cnt_b == 2)):
                res += 'c'
                cnt_c += 1
                cnt_a = cnt_b = 0
                c -= 1
            else:
                break

        return res




