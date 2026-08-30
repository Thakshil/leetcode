class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        x=nums.index(max(nums))
        y=nums.index(min(nums))
        left=max(x,y)+1
        right=len(nums)-min(x,y)
        both=min(x,y)+1+len(nums)-max(x,y)
        return min(left,right,both)
        