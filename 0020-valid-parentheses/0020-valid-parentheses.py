class Solution:
    def isValid(self, s: str) -> bool:
        a="({["
        b=[]
        for i in s:
            if i in a:
                b.append(i)
            elif i==")" and len(b)!=0 and b[-1]=="(":
                b.pop()
            elif i=="}" and len(b)!=0 and b[-1]=="{":
                b.pop()
            elif i=="]" and len(b)!=0 and b[-1]=="[":
                b.pop()
            else:
                return False
        return len(b)==0