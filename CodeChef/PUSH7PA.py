# cook your dish here
import collections
t = int(input())

while t!=0:
	n=int(input())
	l=list(map(int,input().split()))
	f=[[0,0]]
	counter=collections.Counter(l)
	m=[]
	for x,y in counter.items():
		m.append(x+y)
	print(max(m)-1)
	t-=1