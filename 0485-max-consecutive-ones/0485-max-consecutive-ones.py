class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=""
        for i in nums:
            a+=str(i)
        b=a.split("0")
        d=[]
        for i in b:
            d.append(len(i))
        return max(d)