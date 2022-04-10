class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a=stones
        a.sort()
        f=0
        if len(a)==1:
            return a[0]
        while len(a)>1:
            if a[-1]==a[-2]:
                a.pop(-2)
                a.pop(-1)
            else:
                a[-1]-=a[-2]
                a.pop(-2)
                a.sort()
        if len(a)==0:
            return 0
        else: return max(a)