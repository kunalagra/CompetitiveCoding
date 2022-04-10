class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for x in nums:
            dict1[x]=0
        for x in nums:
            dict1[x]+=1
        v = list(dict1.values())
        w = list(dict1.keys())
        c=[]
        for x in range(k):
            m=v.index(max(v))
            c.append(w[m])
            w.pop(m)
            v.pop(m)

        return(c)