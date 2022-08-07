# cook your dish here
import string
t = int(input())

for x in range(t):
    n=int(input())
    s = str(input())
    res = s.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T').replace('G', '%temp%').replace('C', 'G').replace('%temp%', 'C')
    print(res)