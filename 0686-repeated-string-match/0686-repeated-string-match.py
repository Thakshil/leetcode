class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        x=""
        for i in range(1, len(b) // len(a) + 3):
            x+=a
            if b in x:
                return i
        return -1

        