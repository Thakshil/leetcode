class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        a=[x for x in nums1 if x%2==0]
        b=[x for x in nums1 if x%2!=0]
        lb=len(b)
        m=min(b) if lb else 0
        can_even=True
        for x in nums1:
            if x%2!=0 and (lb<2 or x==m):
                can_even=False
                break
        can_odd=True
        for x in nums1:
            if x%2==0 and (lb==0 or x<m):
                can_odd=False
                break

        return can_even or can_odd