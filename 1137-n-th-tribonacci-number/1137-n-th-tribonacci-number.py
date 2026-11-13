class Solution:
    def tribonacci(self, n: int) -> int:
        a=[0,1,1]
        for i in range(n):
            a.append(a[-1]+a[-2]+a[-3])
        return a[n]
        
        