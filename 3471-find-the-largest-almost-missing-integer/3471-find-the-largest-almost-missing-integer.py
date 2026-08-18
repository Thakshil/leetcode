class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        x=[]
        for i in range(0,len(nums)-(k-1)):
            x.append(nums[i:i+k])
        z=[]
        for i in nums:
            c=0
            for j in x:
                if i in j:
                    c+=1
            if c==1:
                z.append(i)
        z.sort()
        if z:
            return z[-1]
        return -1
        