class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ls = list(s)
        d1 = dict(zip(ls,range(0,len(ls))))
        lst = []
        for x in d1:
            s1 = list(set(ls[:d1[x]]))
            c = 0
            for el in s1:
                if d1[x]<d1[el]:
                    continue
                else:
                    c +=1
            if len(s1)==c:
                lst.append(d1[x]+1)
        for i in range(len(lst)-1,0,-1):
            lst[i] = lst[i] - lst[i-1]
        return lst