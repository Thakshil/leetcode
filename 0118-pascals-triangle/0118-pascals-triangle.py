class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        x=[[1],[1,1]]
        while len(x)<numRows:
            z=x[-1]
            res=[z[0]]
            for i in range(1,len(z)):
                res.append(z[i-1]+z[i])
            res.append(z[-1])
            x.append(res)
        return x