import sys

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

t = int(input())

for x in range(t):
	n = int(input())
	l =  get_list()
	m=0
	ic=dict()
	for x in l:
		ic[x] = ic.get(x, 0) + 1
		m = max(m, ic[x])
	print(n-m)