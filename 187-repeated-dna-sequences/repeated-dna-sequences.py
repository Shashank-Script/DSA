class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        for i in range(len(s)-10+1):
            dna = s[i:i+10]
            if dna in seen:
                res.add(dna)
            seen.add(dna)
        return list(res)
