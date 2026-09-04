class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(0,len(nums)):
            x=max(nums[:i+1])
            y=min(nums[i:])
            if x-y<=k:
                return i
        return -1