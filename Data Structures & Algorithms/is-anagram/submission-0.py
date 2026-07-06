class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d= Counter(s)
        for i in range(len(s)):
            d[t[i]]-=1
        for v in d.values():
            if v!=0:
                return False
        return True
