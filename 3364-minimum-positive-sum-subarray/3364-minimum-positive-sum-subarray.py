class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        a=1000000000000000000000000000
        for i in range(0,len(nums)):
            for j in range(i+l,len(nums)+1):
                x=nums[i:j]
                if l<=len(x)<=r:
                    if sum(x)>0 and sum(x)<a:
                        a=sum(x)
        if a==1000000000000000000000000000:
            return -1
        return a

        