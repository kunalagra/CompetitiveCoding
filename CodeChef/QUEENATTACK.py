t = int(input())

while t!=0:
	n,x,y=map(int,input().split())
	rc=(n-1)*2
	mi = min(x,y)
	ma = max(x,y)
	a=min(x-1,n-y)
	b=min(n-x,y-1)
	print(rc+mi-1+n-ma+a+b)
	t-=1