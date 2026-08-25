class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        x=max(nums)
        for i in range(1,x+k+1):
            if i*k not in nums:
                return i*k