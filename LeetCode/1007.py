class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        a1 = max(set(tops), key = tops.count)
        a2 = max(set(bottoms), key = bottoms.count)
        a3=len(tops)
        ft=0
        fb=0
        ct=0
        cb=0
        for x in range(0,a3):
            if tops[x] == a1:
                continue
            else:
                if bottoms[x] == a1:
                    ct+=1
                else:
                    ft=1
                    break
        for x in range(0,a3):
            if bottoms[x] == a2:
                continue
            else:
                if tops[x] == a2:
                    cb+=1
                else:
                    fb=1
                    break
        if ft and fb:
            return -1
        elif ft:
            return cb
        elif fb:
            return ct
        else:
            return min(ct,cb)