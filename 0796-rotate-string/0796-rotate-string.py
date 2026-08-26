class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        x=len(s)+1
        y=list(s)
        for i in range(0,len(s)):
            z=y[-1]
            y.pop()
            y.insert(0,z)
            res="".join(y)
            if res==goal:
                return True
        return False
        
