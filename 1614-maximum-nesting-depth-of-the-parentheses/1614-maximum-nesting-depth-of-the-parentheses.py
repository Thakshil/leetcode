class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        r=0
        for i in s:
            if i==")":
                depth-=1
                continue
            if i!="(":
                continue
            depth+=1
            if depth>r:
                r=depth
        return r
            
        