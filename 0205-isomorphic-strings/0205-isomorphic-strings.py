class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x=0
        for i,j in zip(s,t):
            if s.index(i)==t.index(j):
                x+=1
        return x==len(s)
