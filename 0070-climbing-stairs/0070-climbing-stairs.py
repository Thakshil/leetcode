class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a,b=0,1
        for i in range(n):
            a,b=b,a+b
        return b