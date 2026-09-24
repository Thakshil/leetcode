class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        x=[]
        for i in nums:
            y=str(i)
            res=0
            for j in y:
                res+=int(j)
            x.append(res)
        for i in range(0,len(x)):
            if i==x[i]:
                return x[i]
        return -1