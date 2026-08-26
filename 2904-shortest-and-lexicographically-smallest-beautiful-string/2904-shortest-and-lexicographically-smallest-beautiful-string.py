class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        x=[]
        for i in range(0,len(s)):
            if s[i]=="1":
                x.append(i)
        y=[]
        for i in range(0,len(x)-k+1):
            y.append(x[i:i+k])
        if y:
            z=[]
            for i in y:
                z.append([len(s[i[0]:i[-1]+1]),s[i[0]:i[-1]+1]])
            z.sort()
            return z[0][1]
        else:
            return ""
