class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        w1=""
        w2=""
        target=""
        for i in firstWord:
            w1+=str(alpha.index(i))
        for i in secondWord:
            w2+=str(alpha.index(i))
        for i in targetWord:
            target+=str(alpha.index(i))
        w1=int(w1)
        w2=int(w2)
        return w1+w2==int(target)


        