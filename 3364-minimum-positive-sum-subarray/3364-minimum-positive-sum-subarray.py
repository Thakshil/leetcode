class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        a=[]
        for i in range(0,len(nums)):
            for j in range(i+l,len(nums)+1):
                x=nums[i:j]
                if l<=len(x)<=r:
                    a.append(x)
        b=[]
        for i in a:
            if sum(i)>0:
                b.append(sum(i))
        if b:
            return min(b)
        return -1

        