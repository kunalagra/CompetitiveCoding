from math import ceil
t = int(input())

for x in range(t):
	n,x=map(int,input().split())
	if x >n:
		print(0)
	else:
		print(int(ceil((n-x)/4)))