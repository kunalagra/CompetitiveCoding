class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum1=0
        for a in range(0, len(s)):
            try:
                if dict1[s[a]] < dict1[s[a+1]]:
                    sum1 = sum1 - dict1[s[a]]
                else:	
                    sum1 = sum1 + dict1[s[a]]
            except:
                sum1 = sum1 + dict1[s[a]]
        return sum1