class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        a = len(mat)
        lst = []
        for x in range(0,a):
            lst.append(sum(mat[x]))                
        n=sorted(lst)
        q=[]
        for x in n[:k]:
            c=lst.index(x)
            q.append(c)
            lst[c]='x'
        return(q)