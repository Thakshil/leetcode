class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        x=[nums[0]]
        y=[nums[1]]
        if len(nums)==2:
            return nums
        else:
            for i in range(2,len(nums)):
                if x[-1]>y[-1]:
                    x.append(nums[i])
                else:
                    y.append(nums[i])
        return x+y