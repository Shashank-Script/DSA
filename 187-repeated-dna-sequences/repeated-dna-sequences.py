class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
            
        seen = set()
        res = set()
        dna_map = {'A':0,'C':1,'G':2,'T':3}
        k = 10
        encode = 0
        for i in range(k):
            encode += (4 ** (k-i-1)) * dna_map[s[i]]
        seen.add(encode)

        for i in range(k,len(s)):
            encode -= (4**9) * dna_map[s[i-k]] 
            encode *= 4
            encode += dna_map[s[i]]
            if encode in seen:
                res.add(s[i+1-k:i+1])
            seen.add(encode)
        return list(res)
