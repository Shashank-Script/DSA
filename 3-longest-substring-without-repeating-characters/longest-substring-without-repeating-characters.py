class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char = set()
        i = 0
        for j in range(len(s)):
            while s[j] in char:
                char.discard(s[i])
                i += 1
            char.add(s[j])
            max_len = max(max_len, j-i+1)
        return max_len
