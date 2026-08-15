class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        x=[]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                x.append(s[i:j])
        d=[]
        for i in x:
            co=0
            for j in i:
                if i.count(j)<=2:
                    co+=1
            if co==len(i):
                d.append([len(i),i])
        d.sort(reverse=True)
        if d:
            return d[0][0]


        