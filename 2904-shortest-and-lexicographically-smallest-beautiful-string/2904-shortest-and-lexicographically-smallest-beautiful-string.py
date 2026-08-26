class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        x=[]
        y=[]
        for i in range(0,len(s)):
            for j in range(i+k,len(s)+1):
                z=s[i:j]
                x.append(z)
        for i in x:
            if i.count("1")==k:
                y.append([len(i),i])
        y.sort()
        if y:
            return y[0][1]
        return ""