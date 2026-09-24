class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        a=[[1],[1,1]]
        while len(a)<rowIndex+1:
            x=a[-1]
            res=[x[0]]
            for i in range(1,len(x)):
                res.append(x[i-1]+x[i])
            res.append(x[-1])
            a.append(res)
        return a[rowIndex]




        