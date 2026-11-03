class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x=max(nums)
        y=0
        for i in nums:
            y+=(x-i)
        return y
        