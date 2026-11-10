
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if len(s) == 0:
            return 0

        x = ["+", "-"]
        dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        sign = ""

        if s[0] in x:
            sign = s[0]
            s = s[1:]

        res = ""

        for i in range(len(s)):
            if s[i] in dig:
                res += s[i]
            else:
                break

        res = res.lstrip("0")

        if len(res) == 0:
            return 0

        fres = 0

        for i in res:
            fres = fres * 10 + (ord(i) - ord("0"))

        if sign == "-":
            fres = -fres

        ma = (2**31) - 1
        mi = -(2**31)

        if fres > ma:
            return ma
        if fres < mi:
            return mi

        return fres
