class Solution:
    def digitSum(self, s: str, k: int) -> str:
        round1=[]
        while len(s) > k:
            round1 = []
            for i in range(0, len(s), k):
                round1.append(s[i:i+k])

            s = ""
            for i in round1:
                x = 0
                for j in i:
                    x += int(j)
                s += str(x)

        return s