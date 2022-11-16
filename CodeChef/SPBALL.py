from functools import cache
import sys
sys.setrecursionlimit(10**9)
@cache
def fac(x):
    if x<=1: return 1
    else:
        return (x * fac(x-1))%mod
mod = 10**9 + 7
for x in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    s = 0
    for x in l:
        s += fac(x)
        s %= mod
    print(s)    
    