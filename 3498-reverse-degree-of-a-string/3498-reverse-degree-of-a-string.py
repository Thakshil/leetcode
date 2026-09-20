class Solution:
    def reverseDegree(self, s: str) -> int:
        a="abcdefghijklmnopqrstuvwxyz"
        b=a[::-1]
        c=0
        for i in range(0,len(s)):
            c+=(b.index(s[i])+1)*(i+1)
        return c

        