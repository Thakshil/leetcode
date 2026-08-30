class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums==sorted(nums):
            return True
        count=0
        y=copy.copy(nums)
        while count<=len(nums):
            z=y[-1]
            y.pop()
            y.insert(0,z)
            count+=1
            if y==sorted(nums):
                return True
        return False
