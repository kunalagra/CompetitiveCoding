class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        r=0
        while (startValue<target):
            r+=1
            if target%2==0:
                target/=2
            else:
                target+=1
        return int(r+startValue-target)