class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lst=[]
        c = strs[0]
        f= True
        d=""
        for i in range(1,len(c)+1):
            lst.append(c[:i])
        for x in lst:
            if f:
                for a in strs:
                    if a.startswith(x):
                        d =x
                        continue
                    else:
                        f=False
                        d=x[:-1]
                        break
        return d