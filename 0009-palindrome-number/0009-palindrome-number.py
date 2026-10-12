class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)[::-1]
        return str(x)==a