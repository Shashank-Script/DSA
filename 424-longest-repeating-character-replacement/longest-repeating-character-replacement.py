class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freq = {}
        max_freq = 0
        i = 0
        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_freq = max(freq[s[j]],max_freq)

            while (j-i+1) - max_freq > k:
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    del freq[s[i]]
                i += 1
            
            max_len = max(j-i+1,max_len)
        return max_len

        # max_len = 0
        # for i in range(len(s)):
        #     freq = {}
        #     for j in range(i,len(s)):
        #         freq[s[j]] = freq.get(s[j], 0) + 1
        #         Len = j - i + 1
        #         max_char = max(freq.values())
        #         if Len - max_char <= k:
        #             max_len = max(Len, max_len)
        #         else:
        #             break
        # return max_len
