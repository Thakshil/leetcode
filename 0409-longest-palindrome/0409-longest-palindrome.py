class Solution:
    def longestPalindrome(self, s: str) -> int:
        a=[]
        for i in set(s):
            a.append(s.count(i))
        odd=0
        for i in a:
            if i%2!=0:
                odd+=1
        if odd > 0:
            return len(s) - odd + 1

        return len(s)