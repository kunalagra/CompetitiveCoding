class Solution:
    def calPoints(self, ops: List[str]) -> int:
        a=[]
        for x in ops:
            if x == "C":
                a.pop(-1)
            elif x == "D":
                a.append(a[-1]*2)
            elif x == "+":
                a.append(a[-1]+a[-2])
            else:
                a.append(int(x))
        return sum(a)