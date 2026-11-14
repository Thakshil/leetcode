class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        a=[]
        for i in range(0,len(nums)):
            for j in range(i+l,len(nums)+1):
                x=nums[i:j]
                if l<=len(x)<=r:
                    if sum(x)>0:
                        a.append(sum(x))
        if a:
            return min(a)
        return -1

        