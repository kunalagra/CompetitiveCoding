# cook your dish here
t = int(input())
while (t!=0):
	n,m = map(int,input().split())
	if n>=m:
		print(n*2-m)
	else:
		print(n)
	t-=1