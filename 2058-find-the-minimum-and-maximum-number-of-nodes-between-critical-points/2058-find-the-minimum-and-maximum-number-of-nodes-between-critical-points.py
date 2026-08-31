# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        x=[]
        cur=head
        while cur:
            x.append(cur.val)
            cur=cur.next
        if len(x)==2:
            return [-1,-1]
        local_max=[]
        local_min=[]
        for i in range(1,len(x)-1):
            if x[i-1]<x[i]>x[i+1]:
                local_max.append(i+1)
            if x[i-1]>x[i]<x[i+1]:
                local_min.append(i+1)
        res=local_max+local_min
        res.sort()
        if len(res)<2:
            return [-1, -1]
        min_dis = min(res[i] - res[i-1] for i in range(1, len(res)))
        max_dis=res[-1]-res[0]
        return [min_dis,max_dis]