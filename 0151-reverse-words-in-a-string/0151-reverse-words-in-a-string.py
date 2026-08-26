class Solution:
    def reverseWords(self, s: str) -> str:
        y=[]
        x=s.split(" ")[::-1]
        for i in x:
            if i=="":
                continue
            else:
                y.append(i)
        return " ".join(y)