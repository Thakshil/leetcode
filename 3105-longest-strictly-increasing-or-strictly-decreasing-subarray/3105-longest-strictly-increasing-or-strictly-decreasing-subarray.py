class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        y=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                x=nums[i:j]
                z=set(x)
                if x==sorted(z):
                    y.append(x)
                if x==sorted(z)[::-1]:
                    y.append(x)
        res=[]
        for i in y:
            res.append(len(i))
        return max(res)

        