class Solution:
    def isValid(self, s: str) -> bool:
        l = int(len(s)/2)
        while l:
            s=s.replace('()','').replace('[]','').replace('{}','')
            l-=1
        return (len(s)==0)