class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counterS, counterT = {}, {}

        for c in range(len(s)):
            counterS[s[c]] = 1 + counterS.get(s[c],0)
            counterT[t[c]] = 1 + counterT.get(t[c],0)
        
        for ch in counterS:
            if counterS[ch] != counterT.get(ch,0):
                return False
        
        return True

        
