class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        x=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                sub=nums[i:j]
                x.append(len(set(sub)))
        res=0
        for i in x:
            res+=i*i
        return res
        