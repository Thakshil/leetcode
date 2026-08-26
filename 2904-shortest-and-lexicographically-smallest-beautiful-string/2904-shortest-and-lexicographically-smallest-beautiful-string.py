class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        x=[]
        for i in range(0,len(s)):
            for j in range(i+k,len(s)+1):
                z=s[i:j]
                if z.count("1")==k:
                    x.append([len(z),z])
        x.sort()
        if x:
            return x[0][1]
        return ""