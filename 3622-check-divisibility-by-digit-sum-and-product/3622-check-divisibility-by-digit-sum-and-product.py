class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=str(n)
        z=0
        m=1
        for i in x:
            z+=int(i)
        for i in x:
            m*=int(i)
        res=z+m
        return n%res==0
        